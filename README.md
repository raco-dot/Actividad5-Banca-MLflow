# Actividad 5 | Prediccion de contratacion de depositos bancarios

**Estado:** proyecto reproducible preparado; ejecutar notebook para generar resultados reales y evidencias de MLflow. No se incluyen metricas inventadas.

## Fuente y objetivo
UCI Machine Learning Repository, Bank Marketing, variante **bank-full.csv** (45.211 observaciones, 17 columnas originales). Fuente: https://archive.ics.uci.edu/dataset/222/bank+marketing . Objetivo `y`: contratacion de deposito a plazo (`yes`/`no`). Datos de campañas telefonicas portuguesas; no son datos de BBVA. Uso exclusivamente educativo.

## Estructura
- `datos/datos_ini/`: el script descarga `bank-full.csv` desde UCI.
- `datos/datos_limp/`: CSV limpio generado por el script.
- `fuentes/datos_prep.py`: descarga, validacion, limpieza y exclusion de `duration`.
- `fuentes/train.py`: pipelines, GridSearchCV, metricas y MLflow.
- `fuentes/entrena.ipynb`: ejecucion guiada en Google Colab.
- `resultados/`: metricas y scores por fold tras ejecucion.
- `graficas/`: ROC, matrices de confusion y distribuciones tras ejecucion.
- `evidencias/`: capturas autenticas de MLflow que debe incorporar el estudiante.
- `CHANGELOG.md`: decisiones de versionado.
- `Reporte_tecnico_Actividad5.pdf`: metodologia y espacios para completar resultados verificados.

## Ejecutar en Google Colab (sin instalaciones locales)
1. Subir `Actividad5_Banca.zip` a Colab (panel Archivos).
2. Ejecutar el notebook `fuentes/entrena.ipynb` **despues de subir el ZIP**, o cargar el notebook desde el ordenador y seguir sus celdas. El notebook descomprime el ZIP y ejecuta el proyecto.
3. La primera celda instala `mlflow` y dependencias dentro del entorno de Colab.
4. Ejecutar todas las celdas. Se descargara el dataset original desde UCI (Colab requiere acceso a Internet).
5. Descargar el ZIP final generado por el notebook; incluir evidencias de MLflow y resultados en la entrega.

## Ejecucion local opcional
`pip install -r fuentes/requirements.txt` y `python fuentes/train.py` desde la raiz del proyecto.

## Decisiones metodologicas
- Se excluye `duration` por fuga temporal: se conoce tras la llamada, no antes de decidir a quien contactar.
- No se descartan las etiquetas `unknown`: representan una categoria informativa; OneHotEncoder la codifica.
- Se eliminan duplicados **exactos**, con cautela: dos llamadas similares no necesariamente son la misma observacion.
- Division estratificada 80/20, semilla 42; GridSearchCV 5 folds estratificados solo sobre entrenamiento; criterio F1.
- Escalado numerico y codificacion categorica se ajustan dentro de Pipeline, evitando leakage entre folds.
- Se comparan regresion logistica y Random Forest; se reportan accuracy, precision, recall, F1 y ROC-AUC.
- Se registran parametros, metricas, graficas y modelos en MLflow local en Colab.
- La evaluacion es predictiva, no causal; no implica que contactar a un cliente cause una contratacion.

## Diccionario de datos resumido
`age` edad; `job` ocupacion; `marital` estado civil; `education` estudios; `default` impago previo; `balance` saldo anual medio; `housing` prestamo hipotecario; `loan` prestamo personal; `contact` canal; `day` dia de contacto; `month` mes; `duration` duracion llamada (excluida); `campaign` contactos durante campaña; `pdays` dias desde contacto anterior (-1 significa no contactado); `previous` contactos previos; `poutcome` resultado campaña anterior; `y` deposito contratado.

**Nota de gobernanza:** variables como edad y estado civil pueden generar riesgos de sesgo. Se incluyen solo para un ejercicio academico; en produccion requieren evaluacion de equidad y cumplimiento normativo.

## Publicacion en GitHub
Crear repositorio, subir el contenido de `Actividad5/` (o la carpeta completa) y conservar el historial de commits. No subir credenciales ni datos de clientes reales. En caso de no poder descargar automaticamente UCI, descargar manualmente `bank.zip` de la pagina oficial, extraer `bank-full.csv` y colocarlo en `datos/datos_ini/`.


## MLflow en Colab (configuracion corregida)
El notebook usa SQLite en /content/mlflow.db y el experimento Actividad5_Banca. Antes de cerrar Colab, exporta el ZIP actualizado con la base y los artefactos en evidencias/. No se incluyen capturas del panel hasta que el usuario las genere.
