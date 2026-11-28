# Historial de cambios

## Actividad 6 — noviembre de 2026

- Recuperación de los modelos de la Actividad 5 y reproducción de diez métricas.
- Definición de objetivos SMART y comparación con tres baselines.
- Validación cruzada estratificada de cinco folds y predicciones OOF.
- Evaluación de 198 escenarios de umbral; selección de Random Forest con umbral 0.14.
- Evaluación de matrices de confusión, ROC-AUC y Precision-Recall sobre prueba histórica.
- Bootstrap pareado (2,000 remuestreos), intervalos de confianza y McNemar con Holm.
- Simulación A/B retrospectiva (1,000 repeticiones) y sensibilidad económica (49 escenarios).
- Registro retrospectivo en MLflow: 16 runs, 87 artefactos y verificación de integridad del modelo candidato.
- Integración del tablero visual y evidencia PDF del notebook. El reporte técnico se incorporará posteriormente por el alumno.
- Entrega simplificada: el notebook ejecutable se incorpora por separado; no se incluyen modelos, HTML ni respaldos intermedios.

## Actividad 5 — antecedente

- Preparación de datos, exclusión de duration, entrenamiento y ajuste de hiperparámetros de regresión logística y Random Forest.
- Selección inicial de regresión logística por su F1, recall e interpretabilidad.
- Conservación de modelos y evidencias para reproducir la evaluación posterior.
