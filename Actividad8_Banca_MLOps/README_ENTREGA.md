# Actividad 8 - Entrega final documentada

Continuacion de Actividad 5, modelo bancario de regresion logistica. **Laboratorio academico; no produccion bancaria.**

## Entregables
- documentos/01_Documento_Tecnico.pdf
- documentos/02_Evidencias_Implementacion.pdf
- documentos/03_Incidentes_y_Runbooks.pdf
- codigo/*.py y configuraciones JSON
- Ejercicio_8_Documentado.ipynb (historico de ejecuciones y documentacion)
- evidencias/ (JSON, JSONL, PNG y HTML Plotly)

## Reproducir en Colab
1. Extraer ZIP, abrir notebook; no pulsar Ejecutar todo: contiene historial de desarrollo y pruebas con efectos.
2. Instalar dependencias: `pip install -r requirements.txt`; reiniciar kernel.
3. Comprobar modelo y ejecutar `python -m pytest tests/test_slo.py` (requiere pytest).
4. Comprobar rutas MLflow: `python codigo/reparar_mlflow.py`; si se trasladaron, `python codigo/reparar_mlflow.py --apply` (crea respaldo de SQLite).
5. Iniciar API V2: `uvicorn codigo.api_v2:app --host 127.0.0.1 --port 8001`.
6. API de simulacion: `uvicorn codigo.api_incidentes:app --host 127.0.0.1 --port 8002`; el runbook se limita al endpoint de simulacion.
7. HTML interactivos en evidencias/ se pueden abrir sin servidor.

## Interpretacion
Las pruebas de 100 solicitudes HTTP son locales en Colab. INC-001/INC-002 son sinteticos; INC-003 usa respuestas HTTP controladas. No hay rollback productivo, ni seguimiento desatendido, ni evidencia de despliegue bancario.

## Portabilidad MLflow
Las rutas de artefactos son absolutas en SQLite. `codigo/reparar_mlflow.py --check` (sin modificacion) y `--apply` (respalda y reconfigura para la carpeta actual). No subir los respaldos SQLite al repositorio publico.
