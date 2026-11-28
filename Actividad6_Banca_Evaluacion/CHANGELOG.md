# Historial de cambios | Actividad 6

## 28 de noviembre de 2026 — Integración de entregables en GitHub

### Documentación y publicación

- Creación de la carpeta `Actividad6_Banca_Evaluacion` dentro del repositorio original de la Actividad 5.
- Incorporación y actualización del README con la metodología, resultados, conclusiones y limitaciones.
- Publicación del notebook ejecutable `evalua (10).ipynb`.
- Publicación de la evidencia documental `Resultados de Notebook Evalua.pdf`.
- Publicación del tablero visual `Dashboard_Actividad6.pdf` como alternativa a Trello, conforme a las indicaciones proporcionadas durante la clase 7.
- Incorporación de `requirements.txt` con las dependencias utilizadas.
- Verificación de la visualización del notebook y su evidencia de ejecución en GitHub.
- Actualización de los enlaces relativos a los entregables.
- Reporte técnico pendiente de incorporación.

## Noviembre de 2026 — Actividad 6: evaluación y validación

### Recuperación y reproducibilidad

- Recuperación de los modelos desarrollados en la Actividad 5.
- Reproducción satisfactoria de diez métricas originales.
- Conservación de la partición histórica de entrenamiento y prueba.
- Evaluación sobre 9,039 registros de prueba.

### Evaluación y optimización

- Definición de objetivos SMART.
- Comparación con tres baselines.
- Validación cruzada estratificada de cinco particiones.
- Generación de 36,156 predicciones Out-of-Fold.
- Evaluación de 198 escenarios de umbral.
- Construcción de matrices de confusión.
- Cálculo de accuracy, precision, recall y F1-score.
- Generación de curvas ROC y Precision-Recall.
- Selección de Random Forest con umbral de decisión de 0.14.

### Validación estadística

- Ejecución de 2,000 remuestreos Bootstrap.
- Cálculo de intervalos de confianza del 95%.
- Comparaciones estadísticas mediante Bootstrap pareado.
- Aplicación de la prueba de McNemar con corrección de Holm.
- Identificación de incertidumbre estadística en el cumplimiento del objetivo de recall.

### Simulación A/B e impacto económico

- Simulación retrospectiva con 850 contactos por estrategia.
- Ejecución de 1,000 simulaciones con diferentes asignaciones aleatorias.
- Comparación de selección aleatoria frente a priorización mediante Random Forest.
- Obtención de un lift promedio de 3.28 veces.
- Evaluación económica mediante supuestos académicos.
- Análisis de sensibilidad con 49 escenarios económicos.

### Registro de experimentos y trazabilidad

- Registro retrospectivo de 16 ejecuciones en MLflow.
- Almacenamiento de 87 artefactos asociados.
- Verificación de integridad del modelo mediante SHA-256.
- Recuperación del modelo candidato y reproducción de sus predicciones.
- Generación de 24 gráficas estáticas.
- Construcción de un dashboard interactivo con siete componentes Plotly.
- Generación de un tablero visual PDF de ocho páginas.

### Selección del modelo candidato

Random Forest con umbral de decisión de 0.14.

| Métrica | Resultado |
|---|---:|
| Accuracy | 83.76% |
| Precision | 38.00% |
| Recall | 61.34% |
| F1-score | 46.93% |
| ROC-AUC | 80.33% |

- Cumplimiento puntual de los tres objetivos SMART.
- Mejora de 9.03 puntos porcentuales en F1-score respecto a la regresión logística original.
- Reducción potencial del 30.77% del volumen de contactos comerciales.
- Recomendación como candidato para validación adicional y eventual piloto controlado.
- Modelo no aprobado para producción.

### Limitaciones documentadas

- Reutilización del conjunto histórico de prueba.
- Indicios de sobreajuste en Random Forest.
- Incertidumbre estadística del recall.
- Simulación A/B retrospectiva sin evidencia causal.
- Supuestos económicos hipotéticos.
- Validación externa pendiente.

## Actividad 5 — Antecedentes del proyecto

- Preparación y depuración de datos de UCI Bank Marketing.
- Exclusión de la variable `duration` para evitar fuga de información.
- Entrenamiento de regresión logística y Random Forest.
- Optimización de hiperparámetros.
- Selección inicial de regresión logística por su F1-score, recall e interpretabilidad.
- Registro de experimentos mediante MLflow.
- Conservación de modelos y evidencias para reproducir la evaluación posterior.

## Continuidad del proyecto

- [Actividad 5 — Entrenamiento y optimización](../README.md)
- [Actividad 6 — Evaluación y validación](README.md)
- [Actividad 8 — MLOps y monitorización](../Actividad8_Banca_MLOps/)

---

Proyecto académico de Gestión de Proyectos de Inteligencia Artificial.

Universidad Tecmilenio.
