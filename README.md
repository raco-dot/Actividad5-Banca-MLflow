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

