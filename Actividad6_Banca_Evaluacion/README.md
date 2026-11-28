# Actividad 6 | Evaluación y validación de modelos de Machine Learning

## Predicción de contratación de depósitos a plazo

**Universidad Tecmilenio**  
**Materia:** Gestión de Proyectos de Inteligencia Artificial  
**Alumno:** Rogelio Aco González  
**Docente:** Luis Ariel Vázquez Piña  

---

## 1. Propósito y antecedentes

Este proyecto da continuidad al modelo de predicción de contratación de depósitos a plazo desarrollado en la Actividad 5, utilizando el conjunto público de datos UCI Bank Marketing.

Mientras que en la Actividad 5 el enfoque principal fue el entrenamiento, ajuste de hiperparámetros y selección de modelos, en esta actividad se profundiza en su evaluación, validación estadística y utilidad potencial para el negocio bancario.

Se comparan los modelos de regresión logística y Random Forest, incorporando diferentes umbrales de decisión y criterios de evaluación técnica y comercial.

## 2. Entregables

| Archivo | Descripción |
|---|---|
| [Notebook de experimentación](evalua%20%2810%29.ipynb) | Código Python y resultados de los experimentos realizados en Google Colab. |
| [Resultados de ejecución del notebook](Resultados%20de%20Notebook%20Evalua.pdf) | Evidencia documental del código, gráficas y resultados experimentales. |
| [Dashboard de resultados](Dashboard_Actividad6.pdf) | Tablero visual de métricas, evaluación, validación y resultados comerciales. |
| Reporte técnico | Pendiente de incorporación. |
| [CHANGELOG](CHANGELOG.md) | Historial de cambios y evolución del proyecto. |
| [Requirements](requirements.txt) | Dependencias y versiones de las bibliotecas utilizadas. |

## 3. Definición del problema

El problema corresponde a una clasificación binaria aplicada al sector financiero:

- Clase 0: el cliente no contrata un depósito a plazo.
- Clase 1: el cliente contrata un depósito a plazo.

Se busca identificar clientes con mayor propensión a contratar el producto, contribuyendo a una mejor priorización de los recursos comerciales.

El conjunto de datos depurado contiene 45,195 registros:

| Conjunto | Registros |
|---|---:|
| Entrenamiento | 36,156 |
| Prueba | 9,039 |
| Total | 45,195 |

Se excluye la variable `duration` para evitar utilizar información que no está disponible antes del contacto comercial.

## 4. Objetivo SMART

Evaluar y validar los modelos desarrollados en la Actividad 5, buscando alcanzar durante la Actividad 6 los siguientes indicadores:

- F1-score igual o superior a 40%.
- Recall igual o superior a 60%.
- Precision igual o superior a 30%.

El F1-score se utiliza como métrica principal, considerando el desbalance de clases y la necesidad de equilibrar la identificación de oportunidades con la eficiencia comercial.

## 5. Metodología experimental

El notebook documenta las siguientes etapas:

1. Recuperación de datos y modelos de la Actividad 5.
2. Reproducción de resultados originales.
3. Definición del objetivo SMART y comparación con baselines.
4. Validación cruzada estratificada de cinco particiones.
5. Generación de predicciones Out-of-Fold.
6. Evaluación de 198 escenarios de umbrales.
7. Evaluación comparativa sobre el conjunto de prueba.
8. Construcción de matrices de confusión y curvas ROC y Precision-Recall.
9. Análisis estadístico mediante Bootstrap y McNemar.
10. Simulación retrospectiva de pruebas A/B.
11. Evaluación económica y análisis de sensibilidad.
12. Registro de experimentos mediante MLflow.
13. Construcción del tablero visual de resultados.

## 6. Resultados de evaluación

| Métrica | RF original | RF ajustado | RL original | RL ajustada |
|---|---:|---:|---:|---:|
| Umbral | 0.50 | 0.14 | 0.50 | 0.62 |
| Accuracy | 89.39% | 83.76% | 75.78% | 86.30% |
| Precision | 65.23% | 38.00% | 27.08% | 42.24% |
| Recall | 20.04% | 61.34% | 63.14% | 46.31% |
| F1-score | 30.66% | 46.93% | 37.90% | 44.18% |
| ROC-AUC | 80.33% | 80.33% | 77.35% | 77.35% |

### Modelo seleccionado

**Random Forest con umbral de decisión de 0.14.**

Es el único escenario evaluado que cumple simultáneamente los tres objetivos SMART mediante sus estimaciones puntuales.

Respecto a la regresión logística original, seleccionada en la Actividad 5, obtiene una mejora de 9.03 puntos porcentuales en F1-score.

## 7. Validación estadística

Se realizaron 2,000 remuestreos Bootstrap y comparaciones pareadas entre modelos.

| Métrica | Resultado | IC 95% |
|---|---:|---:|
| F1-score | 46.93% | 44.67% - 49.15% |
| Precision | 38.00% | 35.78% - 40.28% |
| Recall | 61.34% | 58.46% - 64.14% |

La mejora de F1-score respecto a la regresión logística original presenta un intervalo de confianza de 7.57 a 10.57 puntos porcentuales.

Sin embargo, el intervalo de confianza del recall incluye valores inferiores al objetivo del 60%, por lo que se recomienda realizar una validación adicional.

También se aplicó la prueba de McNemar con corrección de Holm para analizar las diferencias en los errores de clasificación.

## 8. Simulación A/B

Se realizó una simulación retrospectiva comparando dos estrategias con una capacidad comercial equivalente de 850 contactos.

| Indicador | Grupo A: Aleatorio | Grupo B: Random Forest |
|---|---:|---:|
| Contactos | 850 | 850 |
| Contrataciones históricas identificadas | 87 | 314 |
| Conversión histórica | 10.24% | 36.94% |

Principales resultados:

- 227 contrataciones históricas adicionales identificadas.
- Lift de 3.61 veces en la simulación principal.
- Lift promedio de 3.28 veces en 1,000 simulaciones.
- Resultados favorables a Random Forest en todas las simulaciones realizadas.

La simulación es retrospectiva y no demuestra un efecto causal sobre las ventas futuras.

## 9. Impacto potencial en el negocio

Al comparar Random Forest ajustado con la regresión logística original se obtuvieron los siguientes resultados:

| Indicador | RL original | RF ajustado |
|---|---:|---:|
| Contactos seleccionados | 2,467 | 1,708 |
| Contrataciones identificadas | 668 | 649 |
| Contactos sin contratación | 1,799 | 1,059 |

Esto representa una reducción potencial del 30.77% del volumen de contactos, conservando el 97.16% del volumen de contrataciones históricas identificadas por el modelo anterior.

Adicionalmente, se realizó un análisis económico utilizando supuestos académicos de $10 MXN por contacto y $300 MXN de margen por contratación.

- Ventaja económica simulada frente a regresión logística: $1,890 MXN.
- Ventaja económica simulada en el escenario A/B: $68,100 MXN.
- Escenarios de sensibilidad económica evaluados: 49.

Los importes son hipotéticos y no representan beneficios financieros reales de una institución bancaria.

## 10. Registro de experimentos y MLOps

Se utilizó MLflow para documentar los resultados experimentales:

- 16 ejecuciones registradas.
- 87 artefactos asociados.
- Registro de métricas, parámetros y umbrales.
- Conservación de evidencias estadísticas.
- Verificación de integridad del modelo mediante SHA-256.
- Recuperación del modelo y reproducción de sus predicciones.

El notebook y el PDF de ejecución contienen las evidencias de este proceso.

## 11. Tablero visual de resultados

El tablero integra las principales evidencias de evaluación y validación:

- Métricas de clasificación.
- Matrices de confusión.
- Curvas ROC y Precision-Recall.
- Optimización de umbrales.
- Validación cruzada.
- Intervalos de confianza.
- Simulación A/B.
- Evaluación económica.
- Trazabilidad mediante MLflow.

[Consultar tablero visual de resultados en PDF](Dashboard_Actividad6.pdf)

## 12. Reproducibilidad

El notebook fue desarrollado y ejecutado en Google Colab utilizando Python.

Para reproducir el ejercicio desde el inicio se requiere:

1. Consultar las dependencias documentadas en `requirements.txt`.
2. Disponer de los datos y modelos originales generados en la Actividad 5.
3. Configurar las rutas de trabajo correspondientes.
4. Ejecutar las celdas del notebook en orden.

El notebook conserva los resultados de ejecución para facilitar su revisión sin necesidad de repetir todos los experimentos.

Las rutas originales corresponden al entorno de Google Colab y pueden requerir ajustes en otros entornos.

## 13. Limitaciones

- Datos históricos de una entidad bancaria extranjera.
- Reutilización del conjunto de prueba de la Actividad 5.
- Indicios de sobreajuste en Random Forest.
- Incertidumbre estadística respecto al cumplimiento del recall.
- Simulación A/B retrospectiva sin evidencia causal.
- Supuestos económicos hipotéticos.
- Costos completos de implementación no incluidos.
- Validación externa pendiente.

## 14. Conclusiones

La evaluación y validación permitieron reconsiderar la selección realizada en la Actividad 5.

Random Forest con un umbral de 0.14 ofrece un equilibrio favorable entre desempeño predictivo, identificación de oportunidades comerciales y eficiencia en la utilización de recursos.

Se recomienda como candidato para una validación adicional y eventual piloto controlado.

**El modelo no se considera aprobado para producción.**

## 15. Continuidad del proyecto

Este ejercicio forma parte de un proyecto académico que aborda diferentes etapas del ciclo de vida de los modelos de inteligencia artificial:

- [Actividad 5: Entrenamiento y optimización de modelos](../README.md)
- Actividad 6: Evaluación y validación de modelos.
- [Actividad 8: MLOps y monitorización](../Actividad8_Banca_MLOps/)

## 16. Fuente de datos

UCI Machine Learning Repository - Bank Marketing.

https://archive.ics.uci.edu/dataset/222/bank+marketing

---

Proyecto académico desarrollado para la materia Gestión de Proyectos de Inteligencia Artificial.
