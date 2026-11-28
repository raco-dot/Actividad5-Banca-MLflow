# Actividad 6 | Evaluación y validación de modelos de Machine Learning

**Predicción de contratación de depósitos a plazo**  
Universidad Tecmilenio · Gestión de Proyectos de Inteligencia Artificial  
Alumno: Rogelio Aco González · Docente: Luis Ariel Vázquez Piña

## Propósito

Este proyecto continúa la Actividad 5 y evalúa regresión logística y Random Forest sobre el conjunto público UCI Bank Marketing. El objetivo SMART establece F1 ≥ 0.40, recall ≥ 0.60 y precision ≥ 0.30. Se excluye `duration` para evitar utilizar información posterior al inicio del contacto.

## Entregables

- Reporte técnico — pendiente de elaboración por el alumno; se incorporará posteriormente.
- [Notebook ejecutable](evalua.ipynb) — se incorpora por separado al repositorio.
- [Notebook de experimentación (PDF)](Notebook_Experimentacion.pdf) — evidencia complementaria de 141 páginas; la impresión presenta recortes y no incluye todas las celdas finales del dashboard.
- [Tablero visual (PDF)](Dashboard_Actividad6.pdf) — alternativa visual a Trello conforme a la aclaración de clase.
- [Historial de cambios](CHANGELOG.md)
- [Dependencias](requirements.txt)

## Metodología

Se recuperaron los modelos de la Actividad 5 y se reprodujeron diez métricas históricas. Se utilizaron 45,195 registros (36,156 de entrenamiento y 9,039 de prueba), semilla 42 y partición estratificada 80/20. Se compararon tres baselines, se generaron predicciones OOF mediante cinco folds por modelo y se evaluaron 198 combinaciones de umbral. La selección se realizó en OOF, no mediante ajuste sobre prueba. Se aplicaron 2,000 remuestreos bootstrap pareados, McNemar con corrección de Holm, 1,000 simulaciones A/B retrospectivas y 49 escenarios económicos. MLflow registró 16 runs y 87 artefactos asociados.

## Resultados sobre prueba histórica

| Modelo | Umbral | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| RF original | 0.50 | 89.39% | 65.23% | 20.04% | 30.66% | 80.33% |
| RF ajustado | 0.14 | 83.76% | 38.00% | 61.34% | 46.93% | 80.33% |
| RL original | 0.50 | 75.78% | 27.08% | 63.14% | 37.90% | 77.35% |
| RL ajustada | 0.62 | 86.30% | 42.24% | 46.31% | 44.18% | 77.35% |

Random Forest ajustado cumple puntualmente las tres metas SMART. Su matriz de confusión contiene 6,922 VN, 1,059 FP, 409 FN y 649 VP. La mejora de F1 frente a la regresión logística original es de 9.03 puntos porcentuales. El IC 95% del recall (58.46–64.14%) incluye valores inferiores a la meta.

## Impacto comercial potencial

Frente a la regresión logística original, Random Forest ajustado reduce los contactos de 2,467 a 1,708 (30.77% menos), identificando 649 frente a 668 contrataciones históricas. La simulación A/B con 850 contactos por grupo identifica 87 frente a 314 contrataciones, con lift de 3.61; el lift promedio de las 1,000 simulaciones es 3.28. Con supuestos de $10 MXN por contacto y $300 MXN por contratación, la ventaja económica simulada es $1,890 frente a RL original y $68,100 frente a la selección aleatoria en A/B. Contactar a todos maximiza el beneficio absoluto bajo esos supuestos, pero requiere mayor capacidad.

## Reproducción

El notebook original se ejecutó en Google Colab con Python 3.13.18. Las dependencias principales están en `requirements.txt`; no constituyen un lockfile completo. Para ejecutar desde el inicio se requiere además el respaldo original `Actividad5_Banca_resultados(2).zip`, con los datos depurados, modelos serializados y resultados históricos. Este respaldo no forma parte de la entrega simplificada. Debe obtenerse por un medio autorizado y cargarse en la primera celda. Ejecutar las celdas en orden. La instalación de MLflow se realiza en la etapa 10. Solo deben deserializarse modelos de origen confiable. Las rutas de almacenamiento de MLflow corresponden a Colab.

Fuente pública del dataset: [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing). El dataset público por sí solo no sustituye el respaldo requerido por este notebook.

## Conclusión y limitaciones

Se recomienda Random Forest con umbral 0.14 como candidato a validación adicional y eventual piloto controlado, no como modelo aprobado para producción. Persisten indicios de sobreajuste, incertidumbre del recall, reutilización de la prueba histórica y ausencia de validación externa. Las simulaciones no demuestran impacto causal ni rentabilidad real; los costos son hipotéticos y excluyen el costo integral de IA. El proyecto es académico y no representa un modelo oficial de una institución bancaria.
