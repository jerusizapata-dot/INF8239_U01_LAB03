# INF8239_U01 - Ensambles, reduccion dimensional y Green AI

## U01.LAB03 - Ejercicio 02

**Maestro:** Edwin Ramon Jose Nolasco

**Estudiante:** Laudys Jerusi Zapata

**Programa:** Maestria en Ciencia de Datos e Inteligencia Artificial

**Universidad:** Universidad Autonoma de Santo Domingo (UASD)

**Asignatura:** Ciencia de Datos e Inteligencia Artificial

**Practica:** LAB03 - Ensambles, reduccion dimensional y Green AI

---

## Descripcion

Este proyecto corresponde al **LAB03** de la asignatura Ciencia de Datos e Inteligencia Artificial.

La practica aborda tecnicas de **ensamble de modelos**, **reduccion dimensional** y conceptos de **Green AI**, considerando tanto el desempeno de los modelos como aspectos relacionados con el costo computacional y la eficiencia.

## Estructura del proyecto

```text
INF8239_U01_LAB03/
|-- data/
|   |-- raw/
|-- docs/
|-- notebooks/
|   |-- 0_lab03_ensamble_green.ipynb
|   |-- reports/
|-- reports/
|-- src/
|   |-- inf8239_u01/
|       |-- __init__.py
|       |-- green.py
|-- tests/
|   |-- test_green.py
|-- .gitignore
|-- README.md
```

## Dataset

Para el desarrollo del laboratorio se utiliza el conjunto de datos correspondiente a **Pruebas Nacionales 2016-2024**.

El archivo de datos se encuentra en:

```text
data/raw/pruebas_nacionales_2016_2024.csv
```

El dataset se utiliza para desarrollar los experimentos de clasificacion, ensambles, reduccion dimensional y analisis de eficiencia computacional.

## Metodologia

El LAB03 integra diferentes tecnicas de aprendizaje automatico y analisis de datos.

Entre los procedimientos desarrollados se incluyen:

* Preparacion y seleccion de variables.
* Estandarizacion de los datos.
* Clasificacion mediante diferentes modelos.
* Comparacion de modelos individuales y modelos de ensamble.
* Evaluacion mediante metricas de clasificacion.
* Matriz de confusion.
* Reduccion dimensional mediante **t-SNE**.
* Comparacion de diferentes semillas.
* Evaluacion del costo computacional.
* Analisis de **Green AI**.
* Construccion de una frontera de Pareto considerando desempeno y eficiencia.

## Modelos evaluados

Durante el laboratorio se utilizan diferentes modelos de clasificacion:

* Regresion Logistica.
* SVM.
* Random Forest.
* Boosting.

Tambien se realizan comparaciones entre diferentes configuraciones de los modelos para analizar el comportamiento del desempeno y el costo computacional.

## Green AI

El componente de **Green AI** considera el costo computacional asociado al entrenamiento y evaluacion de los modelos.

Se registran indicadores relacionados con:

* Tiempo de entrenamiento.
* Desempeno predictivo.
* Comparacion entre configuraciones de modelos.
* Relacion entre desempeno y eficiencia computacional.

A partir de estos resultados se construye una **frontera de Pareto**, que permite visualizar las configuraciones que representan diferentes compromisos entre desempeno y costo computacional.

Los resultados generados se encuentran en:

```text
notebooks/reports/green_ai_results.csv
notebooks/reports/pareto_frontier.png
```

## Reduccion dimensional

Para explorar la estructura de los datos se utiliza **t-SNE** como tecnica de reduccion dimensional.

Se realizaron experimentos utilizando diferentes semillas para observar la estabilidad de la representacion obtenida.

Las figuras generadas se encuentran en:

```text
notebooks/reports/tsne_seed_42.png
notebooks/reports/tsne_seed_7.png
```

## Resultados

Los resultados principales del laboratorio se generan directamente en el notebook:

```text
notebooks/0_lab03_ensamble_green.ipynb
```

Entre las salidas disponibles se incluyen metricas de clasificacion, matrices de confusion, resultados de los modelos, comparaciones de configuraciones y analisis de eficiencia computacional.

La matriz de confusion del modelo de Regresion Logistica se encuentra en:

```text
notebooks/reports/confusion_matrix_logistic.png
```

Los modelos entrenados y almacenados se encuentran en:

```text
notebooks/reports/models/
```

## Ejecucion del proyecto

Para ejecutar el proyecto se recomienda utilizar un entorno virtual de Python.

Activar el entorno virtual:

```bat
.venv\Scripts\activate
```

Instalar las dependencias:

```bat
pip install -r requirements.txt
```

Ejecutar el notebook:

```bat
jupyter notebook
```

Luego abrir:

```text
notebooks/0_lab03_ensamble_green.ipynb
```

## Pruebas

El proyecto incluye pruebas automatizadas para verificar el funcionamiento del componente de Green AI.

Para ejecutar las pruebas:

```bat
pytest -q
```

Resultado esperado:

```text
2 passed
```

Las pruebas se encuentran en:

```text
tests/test_green.py
```

## Codigo reutilizable

La logica relacionada con Green AI se encuentra separada del notebook en:

```text
src/inf8239_u01/green.py
```

Esto permite reutilizar las funciones del proyecto y facilita su validacion mediante pruebas automatizadas.

## Reproducibilidad

El proyecto mantiene separados los datos, notebooks, codigo fuente, pruebas y resultados.

La estructura permite ejecutar nuevamente el notebook y reproducir los principales experimentos realizados durante el laboratorio.

## Repositorio

El codigo fuente y los resultados del LAB03 se encuentran disponibles en el repositorio:

**INF8239_U01_LAB03**

https://github.com/jerusizapata-dot/INF8239_U01_LAB03
