# Proyecto de Machine Learning y MLOps Bancario | Actividades 5, 6 y 8

**Universidad:** Tecmilenio  
**Materia:** Gestión de Proyectos de Inteligencia Artificial  
**Alumno:** Rogelio Aco González  
**Docente:** Luis Ariel Vázquez Piña  
**Repositorio:** https://github.com/raco-dot/Actividad5-Banca-MLflow

## Evolución y estado del proyecto

Este repositorio documenta la evolución de un proyecto académico de inteligencia artificial aplicado a la predicción de contratación de depósitos bancarios, incorporando prácticas de Machine Learning y MLOps a lo largo de su ciclo de vida.

El proyecto integra tres dimensiones complementarias: desarrollo y entrenamiento de modelos, evaluación y validación estadística, y monitorización y observabilidad operativa.

| Actividad | Alcance | Estado |
|---|---|---|
| Actividad 5 | Desarrollo, entrenamiento y optimización de modelos predictivos | Completada |
| Actividad 6 | Evaluación, validación estadística, optimización de umbrales e impacto comercial | Experimentación completada; reporte técnico pendiente de incorporación |
| Actividad 8 | Monitorización, observabilidad y respuesta ante incidentes | Desarrollo y validación técnica completados; publicación parcial |

### Acceso a las actividades

- **Actividad 5:** Los componentes originales se conservan en la raíz de este repositorio.
- **[Actividad 6: Evaluación y validación de modelos](./Actividad6_Banca_Evaluacion/README.md)**
- **[Actividad 8: Monitorización y Observabilidad MLOps Bancaria](./Actividad8_Banca_MLOps/README.md)**

### Ciclo de vida del proyecto

| Etapa | Actividad | Propósito |
|---|---|---|
| Desarrollo | Actividad 5 | Construir, entrenar y optimizar modelos predictivos. |
| Evaluación y validación | Actividad 6 | Analizar su desempeño, incertidumbre estadística y utilidad comercial. |
| Monitorización | Actividad 8 | Supervisar el desempeño predictivo y operativo del modelo de referencia. |

---

# Actividad 5 | Predicción de contratación de depósitos bancarios

**Estado:** entrenamiento y evaluación completados. Datos, programas, resultados, gráficas y evidencias de MLflow publicados en GitHub.

## 1. Descripción y objetivo

Este proyecto desarrolla un ejercicio de aprendizaje automático aplicado a la predicción de contratación de depósitos bancarios, utilizando datos históricos de campañas comerciales.

Se comparan dos algoritmos de clasificación supervisada: **regresión logística y Random Forest**, aplicando preparación de datos, validación cruzada, optimización de hiperparámetros y registro de experimentos mediante MLflow.

El objetivo es evaluar el desempeño de ambos modelos y documentar un proceso reproducible de Machine Learning, incorporando prácticas de MLOps.

Como resultado de esta primera etapa se seleccionó la regresión logística como modelo de referencia, considerando su F1-score, recall e interpretabilidad.

## 2. Fuente de datos

**Dataset:** Bank Marketing  
**Fuente:** UCI Machine Learning Repository  
**Enlace:** https://archive.ics.uci.edu/dataset/222/bank+marketing

Se utiliza la variante `bank-full.csv`, que contiene 45,211 observaciones y 17 columnas originales.

Después del proceso de preparación y depuración se obtuvieron 45,195 registros.

La variable objetivo `y` indica si el cliente contrató un depósito a plazo (`yes` o `no`).

Se excluyó la variable `duration` debido a que representa información que no está disponible antes de realizar el contacto comercial.

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
├── Actividad6_Banca_Evaluacion/
│   ├── CHANGELOG.md
│   ├── Dashboard_Actividad6.pdf
│   ├── README.md
│   ├── Resultados de Notebook Evalua.pdf
│   ├── evalua (10).ipynb
│   └── requirements.txt
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

Los componentes originales de la Actividad 5 se mantienen separados de los correspondientes a las actividades 6 y 8, garantizando la continuidad y trazabilidad del proyecto.

---

# Actividad 6 | Evaluación y validación de modelos de Machine Learning

## 4. Continuidad y objetivo de evaluación

La Actividad 6 profundiza en la evaluación y validación de los modelos desarrollados en la Actividad 5.

El propósito consiste en analizar su desempeño predictivo, capacidad de generalización, incertidumbre estadística y utilidad potencial para una estrategia comercial bancaria.

Se establecieron los siguientes objetivos SMART:

- F1-score igual o superior a 40%.
- Recall igual o superior a 60%.
- Precision igual o superior a 30%.

El F1-score se seleccionó como métrica principal debido al desbalance de clases y a la necesidad de equilibrar la identificación de oportunidades comerciales con la eficiencia de los contactos.

## 5. Funcionalidades y experimentos desarrollados

- Recuperación de los modelos originales de la Actividad 5.
- Reproducción de los resultados experimentales anteriores.
- Comparación con tres baselines.
- Validación cruzada estratificada de cinco particiones.
- Generación de predicciones Out-of-Fold.
- Evaluación de 198 escenarios de umbrales.
- Construcción e interpretación de matrices de confusión.
- Cálculo de accuracy, precision, recall y F1-score.
- Generación de curvas ROC y Precision-Recall.
- Análisis de generalización y posibles indicios de sobreajuste.
- Ejecución de 2,000 remuestreos Bootstrap.
- Cálculo de intervalos de confianza del 95%.
- Comparaciones estadísticas mediante Bootstrap pareado.
- Aplicación de la prueba de McNemar con corrección de Holm.
- Simulación retrospectiva de pruebas A/B.
- Ejecución de 1,000 simulaciones comerciales.
- Evaluación económica y análisis de sensibilidad.
- Registro de experimentos y artefactos mediante MLflow.
- Construcción de un tablero visual de resultados.

## 6. Principales resultados

### Comparación de modelos

| Métrica | RF original | RF ajustado | RL original | RL ajustada |
|---|---:|---:|---:|---:|
| Umbral | 0.50 | 0.14 | 0.50 | 0.62 |
| Accuracy | 89.39% | 83.76% | 75.78% | 86.30% |
| Precision | 65.23% | 38.00% | 27.08% | 42.24% |
| Recall | 20.04% | 61.34% | 63.14% | 46.31% |
| F1-score | 30.66% | 46.93% | 37.90% | 44.18% |
| ROC-AUC | 80.33% | 80.33% | 77.35% | 77.35% |

### Modelo candidato seleccionado

**Random Forest con umbral de decisión de 0.14.**

El modelo cumple puntualmente los tres objetivos SMART y presenta una mejora de 9.03 puntos porcentuales en F1-score respecto a la regresión logística original.

### Validación estadística

| Métrica | Resultado | IC 95% |
|---|---:|---:|
| F1-score | 46.93% | 44.67% - 49.15% |
| Precision | 38.00% | 35.78% - 40.28% |
| Recall | 61.34% | 58.46% - 64.14% |

El intervalo de confianza del recall incluye valores inferiores al objetivo establecido, por lo que se recomienda realizar una validación adicional.

### Impacto comercial y económico

| Indicador | Resultado |
|---|---:|
| Registros del conjunto de prueba | 9,039 |
| Reducción potencial de contactos frente a RL original | 30.77% |
| Volumen de contrataciones históricas identificadas conservado | 97.16% |
| Contrataciones identificadas en el grupo A | 87 |
| Contrataciones identificadas en el grupo B | 314 |
| Contactos por grupo | 850 |
| Lift de la simulación A/B principal | 3.61 veces |
| Lift promedio de 1,000 simulaciones | 3.28 veces |
| Ventaja económica simulada frente a RL | $1,890 MXN |
| Ventaja económica simulada A/B | $68,100 MXN |
| Escenarios de sensibilidad económica | 49 |

Los resultados comerciales corresponden a una simulación retrospectiva y no demuestran un efecto causal sobre las contrataciones futuras.

Los importes económicos se calcularon mediante supuestos académicos y no representan beneficios financieros reales.

### Trazabilidad experimental

| Indicador | Resultado |
|---|---:|
| Celdas de código del notebook | 105 |
| Ejecuciones registradas en MLflow | 16 |
| Artefactos asociados | 87 |
| Gráficas estáticas generadas | 24 |
| Componentes interactivos del dashboard | 7 |
| Páginas del tablero visual PDF | 8 |
| Integridad del modelo candidato | Verificada mediante SHA-256 |
| Reproducción de predicciones | Verificada |

## 7. Documentación y evidencias de la Actividad 6

- [Presentación y documentación de la Actividad 6](./Actividad6_Banca_Evaluacion/README.md)
- [Notebook ejecutable de experimentación](./Actividad6_Banca_Evaluacion/evalua%20%2810%29.ipynb)
- [Resultados de ejecución del notebook en PDF](./Actividad6_Banca_Evaluacion/Resultados%20de%20Notebook%20Evalua.pdf)
- [Tablero visual de resultados](./Actividad6_Banca_Evaluacion/Dashboard_Actividad6.pdf)
- [Historial de cambios](./Actividad6_Banca_Evaluacion/CHANGELOG.md)
- [Dependencias del proyecto](./Actividad6_Banca_Evaluacion/requirements.txt)

El reporte técnico se incorporará posteriormente.

El tablero visual en PDF constituye la alternativa al tablero de Trello indicada durante la clase 7.

## 8. Alcance, limitaciones y recomendación

La evaluación permitió reconsiderar la selección inicial de la Actividad 5.

Random Forest ajustado presenta un equilibrio favorable entre desempeño predictivo, identificación de oportunidades comerciales y eficiencia en la utilización de recursos.

Sin embargo, se reconocen las siguientes limitaciones:

- Reutilización del conjunto histórico de prueba.
- Indicios de sobreajuste en Random Forest.
- Incertidumbre estadística en el cumplimiento del recall.
- Ausencia de una validación externa independiente.
- Simulación A/B retrospectiva sin evidencia causal.
- Supuestos económicos hipotéticos.
- Costos completos de implementación no incluidos.

Se recomienda Random Forest con umbral de 0.14 como candidato para validación adicional y eventual piloto controlado.

**El modelo no se considera aprobado para producción.**

La reproducción integral del notebook requiere los datos, modelos y respaldos originales de la Actividad 5, así como la adaptación de las rutas de trabajo al entorno de ejecución.

---

# Actividad 8 | Monitorización y Observabilidad MLOps Bancaria

## 9. Continuidad del proyecto

La Actividad 8 amplía el proyecto desarrollado en la Actividad 5, incorporando mecanismos de supervisión de la calidad predictiva, monitorización del servicio de inferencia, detección de anomalías y respuesta ante incidentes.

El ejercicio representa la transición desde el desarrollo y evaluación de un modelo de Machine Learning hacia su mantenimiento y supervisión operativa en un entorno académico controlado.

Para esta actividad se utilizó como referencia la regresión logística seleccionada originalmente en la Actividad 5.

Los resultados de la Actividad 6 permiten identificar a Random Forest ajustado como un nuevo candidato. Sin embargo, su incorporación al esquema de monitorización desarrollado en la Actividad 8 requeriría una validación y adaptación posteriores.

## 10. Funcionalidades desarrolladas

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

## 11. Principales resultados

| Indicador | Resultado |
|---|---:|
| Registros del dataset limpio | 45,195 |
| F1-score de referencia | 0.379 |
| Recall | 63.14% |
| Precisión | 27.08% |
| Accuracy | 75.78% |
| Solicitudes HTTP de la API V2 | 100 |
| Respuestas HTTP 200 | 95 |
| Respuestas HTTP 422 esperadas | 5 |
| Disponibilidad técnica observada | 100% |
| Incidentes simulados | 3 |
| Ejecuciones registradas en MLflow | 7 |
| Artefactos MLflow validados | 10 |
| Pruebas funcionales del runbook | 2 de 2 superadas |

## 12. Documentación y evidencias

- [Presentación de la Actividad 8](./Actividad8_Banca_MLOps/README.md)
- [Documentación técnica](./Actividad8_Banca_MLOps/README_TECNICO.md)
- [Instrucciones de entrega](./Actividad8_Banca_MLOps/README_ENTREGA.md)
- [Informe académico y documentos complementarios](./Actividad8_Banca_MLOps/documentos/)
- [Evidencias de implementación](./Actividad8_Banca_MLOps/evidencias/)
- [Artefactos de MLflow](./Actividad8_Banca_MLOps/mlflow_artifacts/)
- [Dataset procesado](./Actividad8_Banca_MLOps/datos/)

## 13. Alcance y limitaciones de publicación

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

---

# Conclusiones generales del proyecto

Las actividades 5, 6 y 8 permiten abordar diferentes etapas del ciclo de vida de un proyecto de inteligencia artificial aplicado al sector bancario.

La Actividad 5 establece los fundamentos del desarrollo y entrenamiento de modelos predictivos.

La Actividad 6 demuestra la importancia de evaluar los modelos mediante diferentes métricas, optimizar los umbrales de decisión, analizar la incertidumbre estadística y relacionar los resultados técnicos con los objetivos del negocio.

La Actividad 8 incorpora mecanismos de monitorización, observabilidad y respuesta ante incidentes, necesarios para supervisar el comportamiento de un modelo durante su operación.

En conjunto, estas actividades permiten comprender que el desarrollo de una solución de inteligencia artificial no termina con el entrenamiento del modelo, sino que requiere un proceso continuo de evaluación, validación, trazabilidad, supervisión y mejora.

Los resultados corresponden a un proyecto académico desarrollado con datos públicos y no representan una implementación productiva de una institución financiera.

## Historial de cambios

La evolución del proyecto y sus principales decisiones técnicas se documentan en los siguientes archivos:

- [CHANGELOG general del proyecto](./CHANGELOG.md)
- [CHANGELOG de la Actividad 6](./Actividad6_Banca_Evaluacion/CHANGELOG.md)

---

**Tecmilenio — 2026**  
**Gestión de Proyectos de Inteligencia Artificial**
