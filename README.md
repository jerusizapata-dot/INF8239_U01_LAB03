# INF8239_U01 - Ensambles, reducción dimensional y Green AI

## U01.LAB03 - Ejercicio 02

**Maestro:** Edwin Ramón José Nolasco
**Estudiante:** Laudys Jerusi Zapata
**Programa:** Maestría en Ciencia de Datos e Inteligencia Artificial
**Universidad:** Universidad Autónoma de Santo Domingo (UASD)
**Asignatura:** Ciencia de Datos e Inteligencia Artificial
**Práctica:** LAB03 - Ensambles, reducción dimensional y Green AI

---

## Descripción

Este proyecto corresponde al **LAB03** de la asignatura Ciencia de Datos e Inteligencia Artificial.

La práctica aborda técnicas de **ensamble de modelos**, **reducción dimensional** y conceptos de **Green AI**, considerando tanto el desempeño de los modelos como aspectos relacionados con el costo computacional y la eficiencia.

## Estructura del proyecto

```text
INF8239_U01_LAB03/
├── data/
│   └── raw/
├── docs/
├── notebooks/
│   ├── 0_lab03_ensamble_green.ipynb
│   └── reports/
│       ├── confusion_matrix_logistic.png
│       ├── green_ai_results.csv
│       ├── pareto_frontier.png
│       ├── tsne_seed_42.png
│       ├── tsne_seed_7.png
│       └── models/
├── reports/
│   └── models/
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       └── green.py
├── tests/
│   └── test_green.py
├── .gitignore
└── README.md
```

## Dataset

Para el desarrollo del laboratorio se utiliza el conjunto de datos correspondiente a **Pruebas Nacionales 2016-2024**.

El archivo de datos se encuentra en:

```text
data/raw/pruebas_nacionales_2016_2024.csv
```

El dataset se utiliza para desarrollar los experimentos de clasificación, ensambles, reducción dimensional y análisis de eficiencia computacional.

## Metodología

El LAB03 integra diferentes técnicas de aprendizaje automático y análisis de datos.

Entre los procedimientos desarrollados se incluyen:

* Preparación y selección de variables.
* Estandarización de los datos.
* Clasificación mediante diferentes modelos.
* Comparación de modelos individuales y modelos de ensamble.
* Evaluación mediante métricas de clasificación.
* Matriz de confusión.
* Reducción dimensional mediante **t-SNE**.
* Comparación de diferentes semillas.
* Evaluación de costo computacional.
* Análisis de **Green AI**.
* Construcción de una frontera de Pareto considerando desempeño y eficiencia.

## Modelos evaluados

Durante el laboratorio se utilizan diferentes modelos de clasificación, entre ellos:

* Regresión Logística.
* SVM.
* Random Forest.
* Boosting.

También se realizan comparaciones entre diferentes configuraciones de los modelos para analizar el comportamiento del desempeño y el costo computacional.

## Green AI

El componente de **Green AI** considera aspectos relacionados con la eficiencia computacional de los modelos.

Se registran variables como:

* Tiempo de entrenamiento.
* Tiempo de predicción.
* Métricas de desempeño.
* Comparación entre modelos.
* Relación entre desempeño y costo computacional.

Los resultados se almacenan en:

```text
notebooks/reports/green_ai_results.csv
```

La frontera de Pareto se encuentra en:

```text
notebooks/reports/pareto_frontier.png
```

## Reducción dimensional

El laboratorio utiliza **t-SNE** como técnica de reducción dimensional para visualizar los datos en un espacio de menor dimensión.

Se realiza
