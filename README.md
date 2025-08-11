# Lab: Puesta en Producción de Modelos TensorFlow (UTKFace Age)

## Integrantes

Darlyn Bravo
Joel Torrejón
Giovanny Vega
Brandon Valle

Este repo contiene los notebooks y el script de inferencia para:
- **Ejercicio 1–4** (tensores, métricas, clasificación)
- **Ejercicio 5**: **predicción de edad** con **UTKFace** + **despliegue mínimo** vía script CLI (`predict_age.py`).

## Requisitos
- Docker y Docker Compose.

## Cómo correr (JupyterLab en Docker)

```bash
# construir la imagen
docker compose build

# levantar JupyterLab
docker compose up
# abre http://localhost:8888