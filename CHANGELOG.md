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



---

# Actividad 8 — Monitorización y Observabilidad MLOps Bancaria

## Continuidad del proyecto

La Actividad 8 da continuidad al proyecto desarrollado en la Actividad 5, incorporando mecanismos de monitorización, observabilidad, mantenimiento y respuesta ante incidentes sobre el modelo de predicción de contratación de depósitos bancarios.

Se mantienen los antecedentes, datos, resultados y evidencias de la actividad anterior, ampliando el alcance hacia la supervisión operativa del modelo de Machine Learning.

## Versión 2.0 — Reconstrucción del modelo y preparación del entorno

**Estado:** Entorno académico preparado y modelo funcional.

### Actividades realizadas

- Recuperación del dataset limpio de la Actividad 5.
- Reconstrucción del modelo de regresión logística.
- Serialización del modelo mediante Joblib.
- Preparación del entorno de ejecución en Google Colab.
- Definición de dependencias mediante requirements.txt.
- Organización de carpetas de código, datos, documentación y evidencias.

### Métricas de referencia

| Métrica | Resultado |
|---|---:|
| Accuracy | 0,7578 |
| Precision | 0,2708 |
| Recall | 0,6314 |
| F1-score | 0,3790 |

### Decisiones

Se utilizó la regresión logística como modelo de referencia por su mayor recall y F1-score respecto al Random Forest evaluado en la Actividad 5.

## Versión 2.1 — Monitorización y detección de data drift

**Estado:** Monitorización académica funcional.

### Actividades realizadas

- Implementación del programa monitor.py.
- Establecimiento de métricas de referencia del modelo.
- Simulación de degradación de la calidad predictiva.
- Simulación de incremento de latencia.
- Detección de cambios en la distribución de la variable balance.
- Aplicación de la prueba estadística Kolmogorov-Smirnov.
- Registro de métricas, incidentes y evidencias en MLflow.

### Resultados

- F1 de referencia: 0,3790.
- F1 durante la degradación simulada: 0,1022.
- Estadístico KS: aproximadamente 0,9756.
- Evidencia de recuperación de los indicadores de referencia en los escenarios simulados.

### Decisiones

Se establecieron mecanismos diferenciados para detectar degradación predictiva, cambios en los datos y problemas operativos del servicio.

## Versión 2.2 — SLO, presupuestos de error y alertamiento inteligente

**Estado:** Reglas de supervisión y alertamiento validadas.

### Objetivos de nivel de servicio

| Indicador | Objetivo académico |
|---|---|
| Disponibilidad | Mayor o igual al 99 % |
| Latencia | Al menos 95 % de solicitudes en 500 ms o menos |
| Calidad predictiva | F1-score mayor o igual a 0,30 |

### Actividades realizadas

- Implementación del cálculo de presupuestos de error.
- Definición de alertas con prioridades P1, P2 y P3.
- Implementación de mecanismos de deduplicación.
- Configuración de cooldown de 300 segundos.
- Validación mediante escenarios sintéticos.
- Integración lógica de indicadores y alertas.

### Decisiones

Se incorporó un mecanismo de reducción de ruido para evitar la emisión repetitiva de alertas sobre una misma condición.

Los umbrales establecidos corresponden a objetivos académicos y no representan compromisos de servicio de una entidad bancaria real.

## Versión 2.3 — API de inferencia y observabilidad

**Estado:** Servicios de inferencia y trazabilidad validados.

### Actividades realizadas

- Implementación de servicios REST mediante FastAPI.
- Ejecución de 30 solicitudes HTTP reales contra la API original en Google Colab.
- Desarrollo de una segunda versión instrumentada de la API.
- Registro de latencia, códigos HTTP, timestamps e identificadores de traza.
- Ejecución de 100 solicitudes HTTP contra la API V2.
- Evaluación de disponibilidad y tiempos de respuesta.
- Diferenciación entre errores del cliente y fallos internos.

### Resultados de la API V2

| Indicador | Resultado |
|---|---:|
| Solicitudes ejecutadas | 100 |
| Respuestas HTTP 200 | 95 |
| Respuestas HTTP 422 esperadas | 5 |
| Errores HTTP 5xx | 0 |
| Disponibilidad técnica observada | 100 % |
| Solicitudes superiores a 500 ms | 0 |
| Consumo del presupuesto de disponibilidad | 0 % |
| Consumo del presupuesto de latencia | 0 % |

### Decisiones

Las respuestas HTTP 422 esperadas se clasificaron como errores del cliente y no como fallos internos del servicio, conforme a la definición académica del indicador de disponibilidad.

## Versión 2.4 — Gestión de incidentes y respuesta automatizada

**Estado:** Escenarios de recuperación validados.

### Incidentes documentados

| Incidente | Descripción |
|---|---|
| INC-001 | Degradación simulada de la calidad del modelo |
| INC-002 | Incremento artificial de la latencia |
| INC-003 | Indisponibilidad HTTP 503 controlada |

### Actividades realizadas

- Documentación de procedimientos de respuesta a incidentes.
- Implementación de un servicio independiente de simulación.
- Validación de recuperación manual.
- Desarrollo de un runbook automático.
- Verificación de la recuperación mediante solicitudes HTTP.
- Validación de ausencia de intervención cuando el servicio está sano.

### Resultados

- Secuencia de recuperación automática: HTTP 503, 200 y 200.
- Pruebas funcionales del runbook: 2 de 2 superadas.

### Limitaciones

El runbook ejecuta una acción correctiva sobre un fallo controlado. No constituye un rollback productivo, un reentrenamiento automático ni un sistema de vigilancia continua.

## Versión 2.5 — Dashboards operativos e interactivos

**Estado:** Visualizaciones generadas.

### Actividades realizadas

- Construcción de dashboards mediante Matplotlib.
- Visualización de métricas de calidad del modelo.
- Representación de incidentes antes, durante y después.
- Seguimiento de disponibilidad, latencia y presupuestos de error.
- Desarrollo de un dashboard mediante Streamlit.
- Generación de dos dashboards interactivos mediante Plotly.

### Limitaciones

El servidor Streamlit respondió correctamente mediante HTTP, pero no se consiguió verificar el renderizado de la interfaz a través del proxy de Google Colab.

Los dashboards de Plotly fueron generados como archivos HTML independientes.

Las visualizaciones corresponden a diferentes escenarios y ventanas de prueba académicas.

## Versión 2.6 — Consolidación y validación técnica

**Estado:** Desarrollo y validaciones técnicas completados en Google Colab.

### Actividades realizadas

- Consolidación de programas, modelo, datos y evidencias.
- Verificación de integridad del archivo ZIP.
- Validación de dependencias y compatibilidad del modelo.
- Comprobación de predicciones de la API.
- Validación de reglas de alertamiento y deduplicación.
- Recuperación de registros históricos de MLflow.
- Corrección de rutas de acceso a los artefactos.
- Verificación funcional del runbook automático.
- Elaboración del notebook documentado.
- Preparación de documentación técnica y académica.

### Resultados de MLflow

| Indicador | Resultado |
|---|---:|
| Ejecuciones registradas | 7 |
| Ejecuciones finalizadas correctamente | 7 |
| Artefactos recuperados | 10 |
| Errores durante la recuperación final | 0 |

### Decisiones

Se consolidó el proyecto en un paquete independiente, conservando los registros experimentales y las evidencias de ejecución.

La portabilidad de MLflow requiere adaptar las rutas de los artefactos cuando se cambia el entorno de ejecución.

## Versión 2.7 — Publicación en GitHub

**Fecha:** 25 de noviembre de 2026.

**Estado:** Documentación y evidencias publicadas; publicación técnica parcial.

### Actividades realizadas

- Conservación de los componentes originales de la Actividad 5.
- Creación de la carpeta Actividad8_Banca_MLOps.
- Publicación del README de la Actividad 8.
- Publicación de README_TECNICO.md y README_ENTREGA.md.
- Publicación de requirements.txt.
- Incorporación del dataset limpio.
- Publicación de cuatro documentos PDF.
- Publicación de 24 de los 26 archivos de evidencias.
- Incorporación de mlflow.db.
- Publicación de los diez artefactos de MLflow.
- Conservación de los siete identificadores originales de ejecución.
- Actualización del README general.
- Ampliación del historial de cambios.

### Componentes pendientes de publicación

- Programas Python y modelo serializado de la carpeta codigo.
- Archivo de pruebas automatizadas tests/test_slo.py.
- Notebook Ejercicio_8_Documentado.ipynb.
- Dashboard dashboard_interactivo.html.
- Dashboard dashboard_incidentes_interactivo.html.

Durante la publicación se presentaron errores de carga con el programa monitor.py y los dos archivos HTML.

La causa exacta de estos errores no fue confirmada. Los demás componentes de código y pruebas quedaron pendientes de publicación.

Los archivos se conservan en el respaldo local consolidado del proyecto.

### Repositorio

https://github.com/raco-dot/Actividad5-Banca-MLflow

### Acceso a la Actividad 8

[Actividad8_Banca_MLOps](./Actividad8_Banca_MLOps/)

---

## Consideraciones finales de MLOps y deuda técnica

La Actividad 8 permitió avanzar desde el entrenamiento y evaluación de modelos hacia la monitorización y supervisión de su funcionamiento.

Se identificaron las siguientes oportunidades de evolución:

- Implementar monitorización continua en un entorno productivo.
- Automatizar la ejecución periódica de pruebas.
- Incorporar almacenamiento persistente para métricas y alertas.
- Implementar presupuestos de error sobre ventanas temporales operativas.
- Ampliar la detección de data drift a múltiples variables.
- Incorporar mecanismos reales de rollback y reentrenamiento.
- Integrar pipelines CI/CD para Machine Learning.
- Fortalecer los mecanismos de seguridad y gobernanza.
- Completar la publicación de los componentes técnicos pendientes.
- Verificar la ejecución integral desde el repositorio GitHub.

## Estado final de las actividades 5 y 8

La Actividad 5 documenta el desarrollo, entrenamiento, evaluación y seguimiento experimental de los modelos predictivos.

La Actividad 8 amplía el proyecto mediante mecanismos de monitorización, observabilidad, alertamiento y respuesta ante incidentes.

El desarrollo y las validaciones técnicas se completaron en un entorno académico controlado. La publicación en GitHub de la Actividad 8 es parcial debido a las limitaciones de carga y los componentes pendientes documentados.

El proyecto utiliza exclusivamente datos públicos de UCI Machine Learning Repository con fines académicos.

Tecmilenio — 2026.
