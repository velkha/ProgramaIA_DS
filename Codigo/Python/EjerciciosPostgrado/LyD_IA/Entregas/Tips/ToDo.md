USAR EL DATASET CON EL CSV DESCARGADO

Cargar con pandas
Analizar con seaborn
Plotly para visualizar en paginas

## Objetivos 

Con esta actividad, se pretende que los alumnos obtengan la capacidad de trabajar en equipo y de mantener una interlocución adecuada y enriquecedora con sus colaboradores, además de que adquieran la capacidad de trabajo independiente y autónomo.

Continuando con el lenguaje Python, el trabajo consistirá en crear un notebook en la plataforma Google Colab de manera que esté compartido entre los miembros de un mismo equipo. En el notebook, los alumnos llevarán a cabo un ejemplo de aprendizaje automático de tipo regresión haciendo uso de las librerías de ciencia de datos disponibles para Python. El trabajo es en equipo, por lo que cada miembro puede encargarse de una parte (carga de datos, exploración, modelado, evaluación), pero todos deberían saber cómo funciona la solución entregada al completo.

## Descripción de la actividad

El ejercicio consiste en crear un modelo predictivo con scikit learn para predecir la propina que dejan los clientes en un restaurante.

El dataset se puede cargar con Seaborn haciendo uso de la función:

df = sns.load_dataset(‘tips’)

También puede descargarse en formato CSV y ser cargado con la función ‘read_csv’ de Pandas.

Una vez cargado el ejercicio consistirá en:

1.	Explorar el dataset: tamaño, estadísticas básicas, nulos, etc.
2.	Llevar a cabo alguna visualización univariante y multivariante con Matplotlib y Seaborn.
3.	Crear un modelo con scikit-learn para predecir la columna tip.
4.	Evaluar la precisión del modelo con las métricas de regresión.

La columna tip es una variable continua, por tanto, se trata de un ejercicio de regresión. Con utilizar un modelo básico de regresión es suficiente. No se busca la máxima precisión para este ejercicio, se busca practicar los pasos comunes a la hora de crear modelos con scikit-learn.

##  Pista:

*	Ver el ejercicio de scikit de clasificación de especies de pingüinos realizado en videotutorial.

Extensión y formato
*	Se debe entregar un archivo notebook descargado desde Google Colab.
*	Se valorará la explicación clara y argumentada, con títulos textos en Mark Down, además de comentarios Python, dentro del propio notebook que expliquen cada paso realizado.
*	Si se detecta plagio en el notebook que copie parte de las respuestas de otro alumno, todos los alumnos involucrados obtendrán una calificación para la actividad de 0 puntos.
