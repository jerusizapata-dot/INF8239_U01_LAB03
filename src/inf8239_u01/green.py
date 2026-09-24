import pandas as pd


def pareto_flags(
    df: pd.DataFrame,
    score: str = "f1_macro",
    cost: str = "fit_median_s",
) -> list[bool]:
    """
    Identifica las configuraciones que pertenecen a la frontera de Pareto.

    Se busca:
    - maximizar el score (por defecto, F1 macro)
    - minimizar el costo (por defecto, tiempo mediano de ajuste)

    Una configuración está dominada si existe otra con:
    - score igual o superior,
    - costo igual o inferior,
    - y al menos una mejora estricta.
    """
    flags = []

    for _, row in df.iterrows():
        dominated = (
            (df[score] >= row[score])
            & (df[cost] <= row[cost])
            & (
                (df[score] > row[score])
                | (df[cost] < row[cost])
            )
        ).any()

        flags.append(not bool(dominated))

    return flags