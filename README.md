# Actividad 5 | Predicción de contratación de depósitos bancarios

**Estado del proyecto:** entrenamiento y evaluación completados. Datos, programas, resultados, gráficas y evidencias de MLflow publicados en GitHub.

**Repositorio:** https://github.com/raco-dot/Actividad5-Banca-MLflow

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

## 3. Estructura del repositorio

```text
Actividad5-Banca-MLflow/
├── datos/
│   ├── datos_ini/
│   │   ├── bank-full.csv
│   │   └── DESCARGA.txt
│   └── datos_limp/
│       ├── bank_marketing_limpio.csv
│       └── LEEME.txt
├── fuentes/
│   ├── datos_prep.py
│   ├── train.py
│   └── entrena.ipynb
├── resultados/
│   └── comparacion_modelos.csv
├── graficas/
│   ├── balance_outliers.png
│   ├── distribucion_clases.png
│   ├── comparacion_metricas.png
│   ├── matriz_Regresion_logistica.png
│   ├── matriz_Random_forest.png
│   ├── roc_Regresion_logistica.png
│   └── roc_Random_forest.png
├── evidencias_mlflow/
│   ├── 01_ejecuciones_metricas.png
│   ├── 02_hiperparametros.png
│   └── 03_artefactos.png
├── README.md
├── CHANGELOG.md
└── Reporte_tecnico_Actividad5.pdf
```

Los archivos `.gitkeep` permiten conservar las carpetas en GitHub.

## 4. Preparación y limpieza de datos

El dataset original contiene 45.211 observaciones.

Durante la preparación se identificaron y eliminaron 16 registros duplicados exactos, obteniéndose 45.195 observaciones.

El proceso contempla:

- Revisión de valores ausentes y tipos de datos.
- Identificación y eliminación de duplicados exactos.
- Conservación de categorías `unknown`.
- Exclusión de la variable `duration` para evitar fuga temporal de información.
- Codificación de variables categóricas mediante OneHotEncoder.
- Escalado de variables numéricas cuando corresponde.
- Preparación de los datos mediante pipelines de scikit-learn.

Las transformaciones estadísticas se ajustan únicamente con los datos de entrenamiento de cada fold, evitando utilizar información de validación.

### Distribución de la variable objetivo

| Categoría | Observaciones |
|---|---:|
| No contratación | 39.906 |
| Contratación | 5.289 |
| Total | 45.195 |

La prevalencia positiva es aproximadamente del **11,70 %**, lo que evidencia un desequilibrio entre clases.

## 5. Modelos y metodología

Se seleccionaron dos algoritmos con enfoques diferentes.

**Regresión logística:** modelo lineal e interpretable que permite establecer una referencia de clasificación y analizar la capacidad de identificar clientes con probabilidad de contratación.

**Random Forest:** modelo basado en conjuntos de árboles de decisión, capaz de capturar relaciones no lineales e interacciones entre variables.

### Configuración experimental

- División estratificada: 80 % entrenamiento y 20 % prueba.
- Semilla aleatoria: 42.
- Validación cruzada estratificada: 5 folds.
- Optimización de hiperparámetros: GridSearchCV.
- Métrica principal de optimización: F1-score.
- Métricas de evaluación: accuracy, precision, recall, F1-score y ROC-AUC.

### Hiperparámetros seleccionados

| Parámetro | Regresión logística | Random Forest |
|---|---|---|
| `C` | 10.0 | No aplica |
| `class_weight` | balanced | No registrado |
| `n_estimators` | No aplica | 200 |
| `max_depth` | No aplica | 16 |
| `min_samples_leaf` | No aplica | 1 |
| `random_state` | 42 | 42 |
| Validación cruzada | 5 folds | 5 folds |

## 6. Resultados obtenidos

Los resultados corresponden a las ejecuciones finalizadas correctamente y registradas en MLflow.

| Métrica | Regresión logística | Random Forest |
|---|---:|---:|
| Accuracy | 75,78 % | 89,39 % |
| Precision | 27,08 % | 65,23 % |
| Recall | 63,14 % | 20,04 % |
| F1-score | 37,90 % | 30,66 % |
| ROC-AUC | 77,35 % | 80,33 % |

### Interpretación

Random Forest obtuvo mejores resultados en accuracy, precision y ROC-AUC.

Por su parte, la regresión logística presentó mayor recall y F1-score, identificando una proporción considerablemente mayor de las contrataciones reales.

Desde una perspectiva bancaria, la elección del modelo depende del objetivo comercial:

- Si se busca identificar más clientes potencialmente interesados, la regresión logística ofrece mayor sensibilidad.
- Si se busca mayor precisión entre los clientes clasificados como interesados, Random Forest presenta mejores resultados.

Los resultados no demuestran causalidad ni garantizan un incremento de contratación mediante acciones comerciales.

## 7. Registro de experimentos con MLflow

Se utilizó MLflow para registrar parámetros, métricas, ejecuciones y artefactos del entrenamiento.

**Experimento:** `Actividad5_Banca`

**Almacenamiento de seguimiento:** SQLite, mediante `mlflow.db`.

El registro recuperado contiene cinco ejecuciones:

- Dos finalizadas correctamente: regresión logística y Random Forest.
- Tres intentos fallidos asociados a dificultades técnicas durante el desarrollo.

Los intentos fallidos se conservaron como parte de la trazabilidad del proceso.

Durante el proyecto se corrigieron problemas de integración y serialización de modelos, utilizando `cloudpickle` en la versión funcional del entrenamiento.

### Evidencias de MLflow

Las evidencias se encuentran en `evidencias_mlflow/`:

- `01_ejecuciones_metricas.png`: estados y métricas de los experimentos.
- `02_hiperparametros.png`: parámetros registrados para ambos modelos.
- `03_artefactos.png`: comprobación de artefactos recuperados.

Estas evidencias se obtuvieron consultando los registros originales de MLflow mediante su API de Python en Google Colab.

No corresponden a capturas del panel gráfico de MLflow, debido a dificultades de acceso a la interfaz mediante el proxy de Colab.

Los registros y artefactos originales también se conservaron en el respaldo `Actividad5_Banca_resultados.zip`.

## 8. Visualizaciones

La carpeta `graficas/` contiene:

- Distribución de clases.
- Identificación de valores atípicos en saldos.
- Comparación de métricas.
- Matrices de confusión de ambos modelos.
- Curvas ROC de regres
