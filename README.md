
# Proyecto de Machine Learning y MLOps Bancario | Actividades 5 y 8

**Materia:** Gestión de Proyectos de Inteligencia Artificial  
**Repositorio:** https://github.com/raco-dot/Actividad5-Banca-MLflow

## Evolución y estado del proyecto

Este repositorio documenta la evolución de un proyecto académico de inteligencia artificial aplicado a la predicción de contratación de depósitos bancarios, incorporando prácticas de Machine Learning y MLOps a lo largo de su ciclo de vida.

| Actividad | Alcance | Estado |
|---|---|---|
| Actividad 5 | Desarrollo, entrenamiento y evaluación del modelo predictivo | Completada |
| Actividad 8 | Monitorización, observabilidad y respuesta ante incidentes | Desarrollo y validación técnica completados; publicación parcial |

### Acceso a las actividades

- **Actividad 5:** Los componentes originales se conservan en la raíz de este repositorio.
- **[Actividad 8: Monitorización y Observabilidad MLOps Bancaria](./Actividad8_Banca_MLOps/README.md)**

---

# Actividad 5 | Predicción de contratación de depósitos bancarios

**Estado:** entrenamiento y evaluación completados. Datos, programas, resultados, gráficas y evidencias de MLflow publicados en GitHub.

## 1. Descripción y objetivo

Este proyecto desarrolla un ejercicio de aprendizaje automático aplicado a la predicción de contratación de depósitos bancarios, utilizando datos históricos de campañas comerciales.

Se comparan dos algoritmos de clasificación supervisada: **regresión logística y Random Forest**, aplicando preparación de datos, validación cruzada, optimización de hiperparámetros y registro de experimentos mediante MLflow.

El objetivo es evaluar el desempeño de ambos modelos y documentar un proceso reproducible de Machine Learning, incorporando prácticas de MLOps.

## 2. Fuente de datos

**Dataset:** Bank Marketing  
**Fuente:** UCI Machine Learning Repository  
**Enlace:** https://archive.ics.uci.edu/dataset/222/bank+marketing

Se utiliza la variante `bank-full.csv`, que contiene 45.211 observaciones y 17 columnas originales.

La variable objetivo `y` indica si el cliente contrató un depósito a plazo (`yes` o `no`).

Los datos corresponden a campañas comerciales de una entidad bancaria portuguesa. No contienen información de BBVA y se utilizan exclusivamente con fines académicos.

## 3. Estructura general del repositorio

```text
Actividad5-Banca-MLflow/
├── datos/
│   ├── datos_ini/
│   └── datos_limp/
├── fuentes/
│   ├── datos_prep.py
│   ├── train.py
│   └── entrena.ipynb
├── resultados/
├── graficas/
├── evidencias_mlflow/
├── Actividad8_Banca_MLOps/
│   ├── codigo/
│   ├── datos/
│   ├── documentos/
│   ├── evidencias/
│   ├── mlflow_artifacts/
│   ├── mlflow.db
│   ├── requirements.txt
│   ├── README.md
│   ├── README_TECNICO.md
│   └── README_ENTREGA.md
├── README.md
└── CHANGELOG.md
```

Los componentes originales de la Actividad 5 se mantienen separados de los correspondientes a la Actividad 8, garantizando la continuidad y trazabilidad del proyecto.

---

# Actividad 8 | Monitorización y Observabilidad MLOps Bancaria

## 4. Continuidad del proyecto

La Actividad 8 amplía el proyecto desarrollado en la Actividad 5, incorporando mecanismos de supervisión de la calidad predictiva, monitorización del servicio de inferencia, detección de anomalías y respuesta ante incidentes.

El ejercicio representa la transición desde el desarrollo y evaluación de un modelo de Machine Learning hacia su mantenimiento y supervisión operativa en un entorno académico controlado.

## 5. Funcionalidades desarrolladas

- Monitorización de métricas F1, recall, precisión y accuracy.
- Seguimiento de experimentos mediante MLflow.
- Implementación de APIs de inferencia con FastAPI.
- Observabilidad y trazabilidad de solicitudes HTTP.
- Definición de SLO y presupuestos de error.
- Alertamiento inteligente y reducción de ruido mediante cooldown.
- Detección de data drift mediante Kolmogorov-Smirnov.
- Simulación controlada de tres incidentes.
- Runbook de recuperación automática.
- Dashboards operativos e interactivos.
- Validación técnica y reproducibilidad.

## 6. Principales resultados

| Indicador | Resultado |
|---|---:|
| Registros del dataset limpio | 45.195 |
| F1-score de referencia | 0,379 |
| Recall | 63,14 % |
| Precisión | 27,08 % |
| Accuracy | 75,78 % |
| Solicitudes HTTP de la API V2 | 100 |
| Respuestas HTTP 200 | 95 |
| Respuestas HTTP 422 esperadas | 5 |
| Disponibilidad técnica observada | 100 % |
| Incidentes simulados | 3 |
| Ejecuciones registradas en MLflow | 7 |
| Artefactos MLflow validados | 10 |
| Pruebas funcionales del runbook | 2 de 2 superadas |

## 7. Documentación y evidencias

- [Presentación de la Actividad 8](./Actividad8_Banca_MLOps/README.md)
- [Documentación técnica](./Actividad8_Banca_MLOps/README_TECNICO.md)
- [Instrucciones de entrega](./Actividad8_Banca_MLOps/README_ENTREGA.md)
- [Informe académico y documentos complementarios](./Actividad8_Banca_MLOps/documentos/)
- [Evidencias de implementación](./Actividad8_Banca_MLOps/evidencias/)
- [Artefactos de MLflow](./Actividad8_Banca_MLOps/mlflow_artifacts/)
- [Dataset procesado](./Actividad8_Banca_MLOps/datos/)

## 8. Alcance y limitaciones de publicación

El desarrollo y las validaciones técnicas fueron realizados en Google Colab, utilizando un entorno académico controlado y datos públicos.

Durante la publicación en GitHub se presentaron errores de carga en algunos archivos. Por este motivo, permanecen pendientes de publicación los siguientes componentes:

- Programas Python y modelo de la carpeta codigo.
- Pruebas automatizadas de la carpeta tests.
- Notebook documentado de Google Colab.
- Dashboard interactivo operativo en formato HTML.
- Dashboard interactivo de incidentes en formato HTML.

Estos componentes se conservan en el respaldo local consolidado del proyecto.

El repositorio contiene los documentos académicos, las gráficas estáticas, los registros de ejecución, las métricas, el dataset, la base de datos de MLflow y los diez artefactos asociados a las siete ejecuciones.

La ejecución integral desde el repositorio queda pendiente de completar la publicación y adaptar las rutas de MLflow al entorno de ejecución.

## 9. Historial de cambios

La evolución del proyecto y sus principales decisiones técnicas se documentan en el archivo [CHANGELOG.md](./CHANGELOG.md).

---

**Tecmilenio — 2026**  
**Gestión de Proyectos de Inteligencia Artificial**
pdf
```

