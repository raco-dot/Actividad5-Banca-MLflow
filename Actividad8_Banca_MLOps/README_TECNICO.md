# Actividad 8 - Observabilidad MLOps bancaria

**Estado:** proyecto academico consolidado y validado en Google Colab (noviembre 2026). Continuacion de Actividad 5. No representa un servicio bancario en produccion.

## Que contiene
- `documentos/`: documento tecnico, evidencias e informe de incidentes en PDF.
- `Ejercicio_8_Documentado.ipynb`: cuaderno con explicaciones, pruebas y resultados historicos. **No ejecutar todo** sin revisar sus efectos.
- `codigo/`: APIs FastAPI, monitor, SLO, alertas, runbook, dashboards y script de portabilidad MLflow.
- `evidencias/`: resultados JSON/JSONL, figuras PNG y dos HTML interactivos Plotly.
- `mlflow.db` y `mlflow_artifacts/`: siete ejecuciones FINISHED y diez artefactos.

## Resultados comprobados
Modelo de regresion logistica con 45.195 registros y 15 variables. Baseline F1 0,3790; recall 0,6314. API V2: 100 solicitudes locales consecutivas, 95 HTTP 200, cinco 422 esperados, cero 5xx; media 19,19 ms, p95 35,72 ms, maxima 42,60 ms. Objetivos academicos: disponibilidad >=99%, al menos 95% de solicitudes <=500 ms y F1 >=0,30. Incidentes INC-001/INC-002 sinteticos; INC-003 HTTP 503 controlado, con recuperacion automatizada verificada al ejecutar el supervisor. No se implemento rollback productivo ni reentrenamiento automatico.

## Ejecucion reproducible
1. Extraer el ZIP en una carpeta de trabajo.
2. Instalar dependencias: `python -m pip install -r requirements.txt` (se requiere scikit-learn 1.8.0). En Colab, reiniciar el kernel despues de instalar.
3. Verificar rutas MLflow con `python codigo/reparar_mlflow.py --check`. Si se trasladaron: `python codigo/reparar_mlflow.py --apply`; el script realiza respaldo antes de modificar SQLite. No modificar el respaldo original.
4. Ejecutar pruebas disponibles: `python -m pytest tests/test_slo.py` (si pytest esta instalado).
5. Iniciar API V2: `python -m uvicorn codigo.api_v2:app --host 127.0.0.1 --port 8001`.
6. Iniciar simulador aislado: `python -m uvicorn codigo.api_incidentes:app --host 127.0.0.1 --port 8002`. El runbook apunta por defecto al puerto 8002; puede configurarse con `A8_SIM_BASE_URL` o argumento `base_url`.
7. Abrir `evidencias/dashboard_interactivo.html` y `evidencias/dashboard_incidentes_interactivo.html` en navegador. Son vistas historicas interactivas, no streaming.

## Evidencia y limites
Los logs tienen identificadores UUID por solicitud, pero no trazas distribuidas. Los 422 esperados se contabilizan separadamente de los fallos 5xx. Las pruebas de 100 solicitudes fueron locales y secuenciales; no demuestran un SLO sostenido ni carga concurrente. Streamlit arranco y respondio HTTP 200, pero su interfaz no se pudo abrir a traves del proxy Colab (404). MLflow se verifico mediante API, no mediante capturas de su interfaz. No publicar datos privados, secretos, respaldos SQLite ni endpoints de inyeccion de fallos.

Consultar `README_ENTREGA.md` y los PDF para la matriz de evidencias y las interpretaciones detalladas.
