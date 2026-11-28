# CHANGELOG | Proyecto de Machine Learning y MLOps Bancario

## Actividades 5, 6 y 8

## Actividad 5 — Predicción de contratación de depósitos bancarios

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

---

# Actividad 6 — Evaluación y validación de modelos de Machine Learning

## Continuidad del proyecto

La Actividad 6 amplía el proyecto académico de predicción de contratación de depósitos bancarios desarrollado en la Actividad 5, incorporando técnicas de evaluación, validación estadística, optimización de umbrales de decisión y análisis del impacto potencial en el negocio.

El ejercicio complementa las actividades anteriores y fortalece la comprensión del ciclo de vida de los modelos de Machine Learning.

Se conservan los datos, modelos, configuraciones y resultados originales para facilitar la comparación y mantener la trazabilidad experimental.

## Versión 3.0 — Recuperación y reproducibilidad

**Estado:** Datos y modelos originales recuperados y verificados.

### Actividades realizadas

- Recuperación del dataset limpio de la Actividad 5.
- Recuperación de los modelos originales de regresión logística y Random Forest.
- Reconstrucción de la partición estratificada de entrenamiento y prueba.
- Conservación de la semilla aleatoria 42.
- Verificación de las versiones de las bibliotecas utilizadas.
- Reproducción de las métricas originales.
- Organización de carpetas de resultados, gráficas y documentación.

### Resultados

| Indicador | Resultado |
|---|---:|
| Registros del dataset limpio | 45,195 |
| Registros de entrenamiento | 36,156 |
| Registros de prueba | 9,039 |
| Contrataciones en el conjunto de prueba | 1,058 |
| Métricas originales reproducidas | 10 de 10 |

### Decisiones

Se conservaron los modelos originales para analizar el efecto de la evaluación y optimización de umbrales sin modificar inicialmente sus hiperparámetros.

Se reconoce que el conjunto de prueba había sido utilizado previamente en la Actividad 5, lo que limita su independencia respecto al proceso histórico de desarrollo.

## Versión 3.1 — Objetivos SMART y modelos de referencia

**Estado:** Criterios de evaluación definidos y baselines evaluados.

### Actividades realizadas

- Definición del problema de clasificación binaria.
- Establecimiento de objetivos SMART.
- Selección del F1-score como métrica principal.
- Evaluación del baseline de clase mayoritaria.
- Evaluación del baseline de selección aleatoria.
- Evaluación de la estrategia de contactar a todos los clientes.
- Comparación de métricas predictivas y comerciales.

### Objetivos SMART

| Métrica | Objetivo mínimo |
|---|---:|
| F1-score | 40% |
| Recall | 60% |
| Precision | 30% |

### Decisiones

Se seleccionó el F1-score como criterio principal debido al desbalance de clases y a la necesidad de equilibrar la identificación de oportunidades comerciales con la eficiencia de los contactos.

La exactitud no se consideró suficiente como criterio único de selección.

## Versión 3.2 — Validación cruzada y optimización de umbrales

**Estado:** Validación cruzada y selección de umbrales completadas.

### Actividades realizadas

- Implementación de validación cruzada estratificada de cinco particiones.
- Ejecución de diez ajustes de modelos durante la validación cruzada.
- Generación de predicciones Out-of-Fold.
- Comparación del desempeño de entrenamiento y validación.
- Identificación de posibles indicios de sobreajuste.
- Evaluación de 99 umbrales por algoritmo.
- Selección de umbrales mediante los criterios SMART y F1-score.

### Resultados

| Indicador | Resultado |
|---|---:|
| Particiones de validación cruzada | 5 |
| Ajustes de modelos | 10 |
| Registros con predicciones OOF | 36,156 |
| Escenarios de umbral evaluados | 198 |
| Umbral seleccionado para Random Forest | 0.14 |
| Umbral seleccionado para regresión logística | 0.62 |

### Decisiones

La selección de umbrales se realizó mediante predicciones Out-of-Fold del conjunto de entrenamiento, evitando utilizar directamente el conjunto de prueba para su optimización.

El ajuste del umbral modifica la regla de clasificación, pero no los hiperparámetros ni las puntuaciones predictivas del modelo.

## Versión 3.3 — Evaluación comparativa y selección del modelo

**Estado:** Evaluación histórica completada y modelo candidato seleccionado.

### Actividades realizadas

- Construcción de matrices de confusión.
- Cálculo de accuracy, precision, recall y F1-score.
- Evaluación de especificidad.
- Generación de curvas ROC.
- Cálculo del área bajo la curva ROC.
- Generación de curvas Precision-Recall.
- Comparación de los cuatro escenarios de clasificación.
- Evaluación del cumplimiento de los objetivos SMART.

### Resultados

| Métrica | RF original | RF ajustado | RL original | RL ajustada |
|---|---:|---:|---:|---:|
| Umbral | 0.50 | 0.14 | 0.50 | 0.62 |
| Accuracy | 89.39% | 83.76% | 75.78% | 86.30% |
| Precision | 65.23% | 38.00% | 27.08% | 42.24% |
| Recall | 20.04% | 61.34% | 63.14% | 46.31% |
| F1-score | 30.66% | 46.93% | 37.90% | 44.18% |
| ROC-AUC | 80.33% | 80.33% | 77.35% | 77.35% |

### Matriz de confusión del modelo candidato

| Indicador | Resultado |
|---|---:|
| Verdaderos positivos | 649 |
| Verdaderos negativos | 6,922 |
| Falsos positivos | 1,059 |
| Falsos negativos | 409 |

### Decisiones

Se seleccionó Random Forest con un umbral de decisión de 0.14 como nuevo modelo candidato.

Este escenario cumple puntualmente los tres objetivos SMART y obtiene una mejora de 9.03 puntos porcentuales en F1-score respecto a la regresión logística original.

La selección no constituye una aprobación para producción.

## Versión 3.4 — Significancia estadística e incertidumbre

**Estado:** Comparaciones estadísticas completadas.

### Actividades realizadas

- Ejecución de 2,000 remuestreos Bootstrap.
- Cálculo de intervalos de confianza del 95%.
- Comparación de modelos mediante Bootstrap pareado.
- Aplicación de la prueba de McNemar.
- Corrección de Holm para comparaciones múltiples.
- Evaluación de la incertidumbre asociada al cumplimiento de los objetivos SMART.

### Intervalos de confianza del modelo candidato

| Métrica | Resultado | IC 95% |
|---|---:|---:|
| F1-score | 46.93% | 44.67% - 49.15% |
| Precision | 38.00% | 35.78% - 40.28% |
| Recall | 61.34% | 58.46% - 64.14% |

### Comparaciones estadísticas de F1-score

| Comparación | Mejora | IC 95% |
|---|---:|---:|
| RF ajustado frente a RF original | 16.27 pp | 13.14 - 19.54 pp |
| RF ajustado frente a RL original | 9.03 pp | 7.57 - 10.57 pp |
| RF ajustado frente a RL ajustada | 2.74 pp | 1.01 - 4.52 pp |

### Decisiones

Los resultados proporcionan evidencia estadística favorable a Random Forest ajustado en términos de F1-score.

Sin embargo, el intervalo de confianza del recall incluye valores inferiores al objetivo establecido del 60%.

Se recomienda realizar una validación adicional sobre datos independientes antes de considerar una implementación real.

## Versión 3.5 — Simulación A/B e impacto económico

**Estado:** Evaluación comercial retrospectiva y análisis económico completados.

### Actividades realizadas

- Diseño de una simulación retrospectiva A/B.
- Asignación aleatoria de registros a dos grupos.
- Comparación de selección aleatoria y priorización mediante Random Forest.
- Establecimiento de una capacidad equivalente de 850 contactos por estrategia.
- Aplicación de pruebas estadísticas de comparación de proporciones.
- Ejecución de 1,000 simulaciones con diferentes semillas aleatorias.
- Evaluación económica mediante supuestos académicos.
- Análisis de sensibilidad con 49 escenarios económicos.
- Cálculo del punto de equilibrio económico.

### Resultados de la simulación A/B

| Indicador | Grupo A: Aleatorio | Grupo B: Random Forest |
|---|---:|---:|
| Contactos seleccionados | 850 | 850 |
| Contrataciones históricas identificadas | 87 | 314 |
| Conversión histórica | 10.24% | 36.94% |

### Indicadores comerciales y económicos

| Indicador | Resultado |
|---|---:|
| Contrataciones históricas adicionales identificadas | 227 |
| Lift de la simulación principal | 3.61 veces |
| Lift promedio de 1,000 simulaciones | 3.28 veces |
| Reducción potencial de contactos frente a RL original | 30.77% |
| Ventaja económica simulada frente a RL original | $1,890 MXN |
| Ventaja económica simulada A/B | $68,100 MXN |
| Escenarios económicos evaluados | 49 |

### Decisiones y limitaciones

La priorización mediante Random Forest presenta resultados favorables en el ejercicio retrospectivo.

Las simulaciones no constituyen campañas comerciales reales ni demuestran un efecto causal sobre las contrataciones futuras.

Los resultados económicos corresponden a supuestos académicos y no representan información financiera real de una institución bancaria.

La conveniencia económica del modelo depende del costo de contacto, el margen por contratación y las restricciones de capacidad comercial.

## Versión 3.6 — MLflow, trazabilidad y tablero visual

**Estado:** Registro experimental y evidencias visuales completados.

### Actividades realizadas

- Creación del experimento independiente de MLflow para la Actividad 6.
- Registro retrospectivo de métricas, parámetros y configuraciones.
- Conservación de evidencias de validación cruzada.
- Registro de resultados de optimización de umbrales.
- Incorporación de pruebas estadísticas y simulaciones A/B.
- Registro del análisis económico.
- Almacenamiento del modelo candidato.
- Verificación de integridad mediante SHA-256.
- Recuperación del modelo y reproducción de sus predicciones.
- Construcción de un dashboard interactivo mediante Plotly.
- Generación de un tablero visual en PDF.

### Resultados

| Indicador | Resultado |
|---|---:|
| Ejecuciones registradas en MLflow | 16 |
| Ejecuciones finalizadas correctamente | 16 |
| Artefactos asociados | 87 |
| Gráficas estáticas generadas | 24 |
| Componentes interactivos del dashboard | 7 |
| Páginas del tablero visual PDF | 8 |
| Integridad del modelo | Verificada |
| Reproducción de predicciones | Verificada |

### Decisiones

Se conservaron los registros experimentales mediante MLflow para fortalecer la trazabilidad y reproducibilidad del proyecto.

El modelo y su umbral de decisión se documentaron por separado.

El tablero visual PDF se utiliza como alternativa a Trello, conforme a las indicaciones proporcionadas durante la clase 7.

## Versión 3.7 — Publicación e integración en GitHub

**Fecha:** 28 de noviembre de 2026.

**Estado:** Experimentación completada y evidencias publicadas. Reporte técnico pendiente de incorporación.

### Actividades realizadas

- Conservación de los componentes originales de las actividades 5 y 8.
- Creación de la carpeta `Actividad6_Banca_Evaluacion`.
- Publicación del README de la Actividad 6.
- Publicación del CHANGELOG específico.
- Incorporación de requirements.txt.
- Publicación del notebook ejecutable.
- Publicación del PDF con los resultados de ejecución.
- Publicación del tablero visual PDF.
- Verificación de la visualización del notebook y su evidencia documental.
- Actualización del README general del repositorio.
- Integración del historial de cambios de las tres actividades.

### Archivos publicados

- [README de la Actividad 6](./Actividad6_Banca_Evaluacion/README.md)
- [CHANGELOG de la Actividad 6](./Actividad6_Banca_Evaluacion/CHANGELOG.md)
- [Notebook ejecutable](./Actividad6_Banca_Evaluacion/evalua%20%2810%29.ipynb)
- [Resultados de ejecución del notebook](./Actividad6_Banca_Evaluacion/Resultados%20de%20Notebook%20Evalua.pdf)
- [Dashboard de resultados](./Actividad6_Banca_Evaluacion/Dashboard_Actividad6.pdf)
- [Dependencias del proyecto](./Actividad6_Banca_Evaluacion/requirements.txt)

### Alcance de publicación

Se priorizó la publicación de los entregables académicos y las evidencias necesarias para consultar los resultados.

Los modelos serializados, archivos HTML, respaldos intermedios y bases de datos experimentales de la Actividad 6 se conservan como evidencias complementarias fuera de esta carpeta.

La reproducción integral requiere recuperar los datos, modelos y respaldos originales de la Actividad 5 y adaptar las rutas al entorno de ejecución.

### Componentes pendientes

- Incorporación del reporte técnico final.
- Verificación integral de los enlaces del repositorio.
- Consolidación del ZIP definitivo de entrega.

---

## Consideraciones finales de MLOps y deuda técnica de la Actividad 6

Se identificaron las siguientes oportunidades de evolución:

- Realizar una validación externa con datos independientes.
- Investigar y reducir los indicios de sobreajuste de Random Forest.
- Fortalecer la estabilidad del recall.
- Evaluar la calibración de las puntuaciones predictivas.
- Incorporar mecanismos de explicabilidad del modelo.
- Evaluar equidad y posibles sesgos.
- Diseñar una prueba A/B prospectiva bajo condiciones controladas.
- Incorporar los costos completos de implementación y operación.
- Evaluar la integración del nuevo candidato con los mecanismos de monitorización desarrollados en la Actividad 8.
- Mejorar la portabilidad de los registros de MLflow.
- Automatizar las pruebas de evaluación y validación.

## Estado consolidado de las actividades 5, 6 y 8

| Actividad | Alcance | Estado |
|---|---|---|
| Actividad 5 | Desarrollo, entrenamiento y optimización | Completada |
| Actividad 6 | Evaluación y validación estadística | Experimentación completada; reporte técnico pendiente |
| Actividad 8 | Monitorización y observabilidad MLOps | Validación técnica completada; publicación parcial |

### Evolución del modelo

La regresión logística fue seleccionada como modelo de referencia en la Actividad 5 y utilizada en los ejercicios de monitorización de la Actividad 8.

La evaluación realizada en la Actividad 6 permitió seleccionar Random Forest con umbral de 0.14 como nuevo candidato para validación adicional.

Esta decisión no implica que Random Forest haya sido incorporado al servicio de inferencia o al esquema de monitorización de la Actividad 8.

Su eventual incorporación requeriría validaciones y adaptaciones posteriores.

### Acceso a las actividades

- [Actividad 5 — Desarrollo y entrenamiento](./README.md)
- [Actividad 6 — Evaluación y validación](./Actividad6_Banca_Evaluacion/README.md)
- [Actividad 8 — Monitorización y observabilidad](./Actividad8_Banca_MLOps/README.md)

### Repositorio general

https://github.com/raco-dot/Actividad5-Banca-MLflow

---

El proyecto utiliza exclusivamente datos públicos de UCI Machine Learning Repository con fines académicos.

Los modelos, simulaciones comerciales y mecanismos de monitorización desarrollados no constituyen una implementación productiva de una institución financiera.

**Tecmilenio — 2026**

**Gestión de Proyectos de Inteligencia Artificial**
