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

El componente de **Green AI** considera
