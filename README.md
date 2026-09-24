\# INF8239\_U01 - Ensambles, reducción dimensional y Green AI



\## U01.LAB03 - Ejercicio 02



\*\*Maestro:\*\* Edwin Ramón José Nolasco

\*\*Estudiante:\*\* Laudys Jerusi Zapata

\*\*Programa:\*\* Maestría en Ciencia de Datos e Inteligencia Artificial

\*\*Universidad:\*\* Universidad Autónoma de Santo Domingo (UASD)

\*\*Asignatura:\*\* Ciencia de Datos e Inteligencia Artificial

\*\*Práctica:\*\* LAB03 - Ensambles, reducción dimensional y Green AI



\---



\## Descripción



Este proyecto corresponde al \*\*LAB03\*\* de la asignatura Ciencia de Datos e Inteligencia Artificial.



La práctica aborda técnicas de \*\*ensamble de modelos\*\*, \*\*reducción dimensional\*\* y conceptos de \*\*Green AI\*\*, considerando tanto el desempeño de los modelos como aspectos relacionados con el costo computacional y la eficiencia.



\## Estructura del proyecto



```text

INF8239\_U01\_LAB03/

├── data/

├── docs/

├── notebooks/

├── reports/

│   └── models/

├── src/

│   └── inf8239\_u01/

│       └── green.py

├── tests/

│   └── test\_green.py

├── .gitignore

└── README.md

```



\## Requisitos



\* Python 3.13

\* NumPy

\* Pandas

\* Scikit-learn

\* Matplotlib

\* Seaborn

\* Pytest



\## Instalación



Crear el entorno virtual:



```bash

python -m venv .venv

```



Activarlo en Windows:



```bat

.venv\\Scripts\\activate

```



Instalar las dependencias:



```bat

pip install numpy pandas scikit-learn matplotlib seaborn pytest

```



\## Ejecución de las pruebas



El proyecto utiliza una estructura `src/`. En Windows, configurar el acceso al código fuente:



```bat

set PYTHONPATH=src

```



Ejecutar las pruebas:



```bat

pytest -q

```



Resultado obtenido en la verificación del proyecto:



```text

2 passed in 0.41s

```



\## Notebook



Los análisis y experimentos correspondientes al LAB03 se encuentran en:



```text

notebooks/0\_lab03\_ensamble\_green.ipynb

```



Los notebooks deben ejecutarse utilizando el entorno virtual del proyecto.



\## Código fuente



El código reutilizable se encuentra en:



```text

src/inf8239\_u01/green.py

```



Este módulo contiene las funciones desarrolladas para el componente de \*\*Green AI\*\*.



\## Pruebas automatizadas



Las pruebas se encuentran en:



```text

tests/test\_green.py

```



Actualmente, la ejecución de `pytest -q` produce:



```text

2 passed

```



\## Reproducibilidad



Para reproducir el proyecto:



1\. Clonar el repositorio.

2\. Crear el entorno virtual.

3\. Activar el entorno virtual.

4\. Instalar las dependencias.

5\. Configurar `PYTHONPATH=src`.

6\. Ejecutar `pytest -q`.

7\. Ejecutar el notebook ubicado en `notebooks/`.



\## Repositorio



El proyecto se encuentra versionado mediante Git y publicado en GitHub.



\*\*Repositorio:\*\* INF8239\_U01\_LAB03



\*\*Autora:\*\* Laudys Jerusi Zapata



\*\*Universidad:\*\* Universidad Autónoma de Santo Domingo (UASD)



