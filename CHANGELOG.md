CHANGELOG — Actividad 5: Predicción de contratación de depósitos bancarios

Historial de cambios y evolución del proyecto

Este documento registra las principales etapas de desarrollo, decisiones metodológicas, ajustes técnicos y resultados del proyecto de Machine Learning aplicado al dataset Bank Marketing de UCI.

El objetivo del versionamiento es garantizar la trazabilidad de los datos, el código, los experimentos y las evidencias generadas.

Versión 1.0 — Proyecto inicial

Estado: Preparación del entorno y diseño metodológico

Actividades realizadas

Selección del dataset público Bank Marketing de UCI Machine Learning Repository.

Definición del problema de clasificación binaria: predicción de contratación de depósitos a plazo.

Selección de regresión logística y Random Forest como algoritmos comparativos.

Diseño de la estructura del proyecto con carpetas de datos, fuentes, resultados y gráficas.

Preparación de los archivos datos_prep.py, train.py y entrena.ipynb.

Elaboración inicial de README y documentación técnica.

Decisiones

Se seleccionó un caso bancario para aplicar técnicas de aprendizaje automático a un problema comercial, utilizando exclusivamente información pública con fines académicos.

Versión 1.1 — Preparación y limpieza de datos

Estado: Dataset preparado

Actividades realizadas

Obtención del archivo original bank-full.csv, con 45.211 observaciones.

Revisión de estructura, tipos de datos y valores ausentes.

Identificación y eliminación de 16 registros duplicados exactos.

Generación de bank_marketing_limpio.csv, con 45.195 observaciones.

Identificación de desequilibrio en la variable objetivo.

Exclusión de la variable duration para evitar fuga temporal de información.

Conservación de las categorías unknown.

Distribución del objetivo

No contratación: 39.906 registros.

Contratación: 5.289 registros.

Prevalencia positiva: 11,70 %.

Decisiones

Se mantuvieron las variables categóricas y se aplicaron transformaciones mediante pipelines para evitar utilizar información de validación durante el entrenamiento.

Versión 1.2 — Entrenamiento y optimización

Estado: Modelos entrenados y evaluados

Actividades realizadas

Implementación de regresión logística y Random Forest.

División estratificada de datos: 80 % entrenamiento y 20 % prueba.

Configuración de semilla aleatoria 42.

Implementación de GridSearchCV con validación cruzada estratificada de cinco folds.

Optimización utilizando F1-score.

Aplicación de escalado numérico y codificación categórica dentro de pipelines.

Evaluación mediante accuracy, precision, recall, F1-score y ROC-AUC.

Hiperparámetros seleccionados

Regresión logística

C = 10.0

class_weight = balanced

Random Forest

n_estimators = 200

max_depth = 16

min_samples_leaf = 1

Decisiones

La regresión logística se utilizó como modelo lineal de referencia, mientras que Random Forest permitió evaluar relaciones no lineales e interacciones entre variables.

Versión 1.3 — Integración y correcciones de MLflow

Estado: Seguimiento de experimentos funcional

Actividades realizadas

Instalación y configuración de MLflow 3.x en Google Colab.

Configuración del experimento Actividad5_Banca.

Utilización de SQLite mediante mlflow.db.

Unificación de la configuración de seguimiento entre el notebook y train.py.

Identificación de dificultades técnicas durante el registro de modelos.

Corrección del problema de serialización utilizando cloudpickle.

Registro de parámetros, métricas y artefactos.

Conservación del historial de ejecuciones exitosas y fallidas.

Resultado

Se recuperaron cinco ejecuciones del experimento:

Dos ejecuciones finalizadas correctamente.

Tres ejecuciones fallidas durante el proceso de desarrollo.

Decisiones

Se conservaron los intentos fallidos como parte de la trazabilidad experimental y de la documentación de deuda técnica.

Versión 1.4 — Resultados y comparación de modelos

Estado: Evaluación completada

Métricas registradas en MLflow

Métrica

Regresión logística

Random Forest

Accuracy

0.757827

0.893904

Precision

0.270774

0.652308

Recall

0.631380

0.200378

F1-score

0.379007

0.306580

ROC-AUC

0.773500

0.803305

Interpretación

Random Forest obtuvo mejores resultados en accuracy, precision y ROC-AUC.

La regresión logística consiguió mayor recall y F1-score, mostrando una mayor capacidad para identificar contrataciones reales.

La elección del modelo depende del objetivo comercial y del costo relativo de los falsos positivos y falsos negativos.

Archivos generados

resultados/comparacion_modelos.csv

Curvas ROC de ambos modelos.

Matrices de confusión.

Comparación gráfica de métricas.

Distribución de clases.

Visualización de valores atípicos.

Versión 1.5 — Recuperación de experimentos y evidencias

Estado: Evidencias técnicas recuperadas

Actividades realizadas

Recuperación de mlflow.db y mlruns/ desde el ZIP de resultados.

Verificación de las cinco ejecuciones mediante la API de MLflow.

Recuperación de métricas e hiperparámetros registrados.

Identificación y comprobación de artefactos originales.

Detección de diferencias entre las rutas originales y restauradas de los artefactos.

Intentos de acceso a la interfaz visual mediante los puertos 5000 y 5001 de Google Colab.

Confirmación de que el servidor local respondía, aunque el proxy de Colab devolvía HTTP 404.

Evidencias publicadas

evidencias_mlflow/01_ejecuciones_metricas.png

evidencias_mlflow/02_hiperparametros.png

evidencias_mlflow/03_artefactos.png

Limitación documentada

Las evidencias se obtuvieron mediante consultas a los registros originales de MLflow desde Python.

No se consiguieron capturas del panel gráfico debido a dificultades de acceso mediante el proxy de Google Colab.

Versión 1.6 — Publicación en GitHub

Estado: Repositorio académico publicado

Actividades realizadas

Creación del repositorio público Actividad5-Banca-MLflow.

Publicación del dataset original y limpio.

Incorporación de datos_prep.py, train.py y entrena.ipynb.

Publicación de comparacion_modelos.csv.

Incorporación de siete visualizaciones.

Publicación de tres evidencias técnicas de MLflow.

Actualización de README con resultados reales, metodología y limitaciones.

Documentación de cambios en CHANGELOG.

Repositorio

https://github.com/raco-dot/Actividad5-Banca-MLflow

Consideraciones finales de MLOps y deuda técnica

El proyecto permitió aplicar prácticas de reproducibilidad, versionamiento y seguimiento experimental.

Se identificaron las siguientes oportunidades de mejora:

Utilizar almacenamiento persistente para MLflow.

Automatizar pruebas de calidad de datos.

Incorporar controles de versiones especializados para datasets.

Reducir la dependencia de rutas temporales de Google Colab.

Automatizar los pipelines de entrenamiento.

Incorporar monitoreo de desempeño y deriva de datos.

Evaluar equidad y riesgos de sesgo antes de cualquier aplicación bancaria real.

Estado final

Entrenamiento y evaluación completados.

El repositorio contiene los datos, el código, el notebook, las métricas, las visualizaciones y las evidencias técnicas recuperadas de MLflow.

El proyecto se desarrolló exclusivamente con fines académicos utilizando datos públicos de UCI Machine Learning Repository.
