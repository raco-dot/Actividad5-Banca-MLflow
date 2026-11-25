
# Actividad 8 | Monitorización y Observabilidad MLOps Bancaria

## 1. Antecedentes y continuidad del proyecto

Esta actividad da continuidad al proyecto desarrollado en la Actividad 5, referente a la predicción de contratación de depósitos bancarios mediante Machine Learning, utilizando el dataset público Bank Marketing de UCI.

El objetivo general fue desarrollar un sistema de monitorización y observabilidad MLOps aplicado a un modelo de predicción de contratación de depósitos bancarios, 
utilizando el conjunto de datos Bank Marketing y un modelo de regresión logística previamente entrenado.

## 2. Objetivo

Implementar un sistema académico de monitorización proactiva que permita supervisar la calidad predictiva del modelo, evaluar el funcionamiento del servicio de inferencia, detectar anomalías y ejecutar procedimientos de recuperación.

## 3. modulos que contiene la implementación

1 Preparación del entorno

2 Carga y compatibilidad del modelo

3 Monitorización inicial y línea base

4 Seguimiento de experimentos con MLflow

5 Primeras visualizaciones y respaldo

6 SLO, error budgets y alertas inteligentes

7 API original y mediciones HTTP reales

8 API V2: instrumentación y pruebas de 100 solicitudes

9 INC-003: indisponibilidad controlada y runbooks

10 Dashboard Streamlit y limitación de acceso

11 Dashboards interactivos en Plotly


## 4. Objetivos de nivel de servicio

| Indicador | Objetivo  |
|---|---|
| Disponibilidad | Mayor o igual al 99 % |
| Latencia | Al menos 95 % de solicitudes en 500 ms o menos |
| Calidad predictiva | F1-score mayor o igual a 0,30 |

## 5. Principales resultados

| Indicador | Resultado |
|---|---|
| Registros del dataset | 45.195 |
| F1-score de referencia | 37,90 % |
| Recall | 63,14 % |
| Precisión | 27,08 % |
| Accuracy | 75,78 % |
| Solicitudes HTTP API V2 | 100 |
| Respuestas HTTP 200 | 95 |
| Respuestas HTTP 422 esperadas | 5 |
| Disponibilidad técnica API V2 | 100 % |
| Latencia media API V2 | 19,19 ms |
| Latencia p95 | 35,72 ms |
| Latencia p99 | 42,27 ms |
| Ejecuciones MLflow | 7 |
| Artefactos MLflow verificados | 10 |

## 6. Incidentes simulados

| Incidente | Descripción | Resultado |
|---|---|---|
| INC-001 | Degradación sintética del modelo | Recuperación del F1 de referencia |
| INC-002 | Incremento artificial de latencia | Retorno a la latencia de referencia |
| INC-003 | Indisponibilidad HTTP 503 controlada | Recuperación automática a HTTP 200 |

## 7. Herramientas utilizadas

- Python
- Google Colab
- Scikit-learn
- Pandas y NumPy
- FastAPI y Uvicorn
- MLflow y SQLite
- Streamlit
- Plotly y Matplotlib
- GitHub

## 8. Alcance y limitaciones

El proyecto fue desarrollado y validado en un entorno de desarrollo y prueba.

Las solicitudes HTTP fueron ejecutadas contra servicios locales de Google Colab. Los incidentes fueron simulados para validar los mecanismos de detección y recuperación.

Los dashboards representan evidencias de las pruebas realizadas. La monitorización continua en producción, el rollback real y el reentrenamiento automático se plantean como mecanismos de evolución futura.

## 9. Estado del proyecto

Desarrollo funcional y validación técnica completados.

La documentación, el código fuente, el notebook y las evidencias se incorporarán a esta carpeta.

---

Materia: Gestión de Proyectos de Inteligencia Artificial

Actividad 8: Monitorización, mantenimiento y gobernanza operativa.
