FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git wget curl ca-certificates unzip \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install \
    jupyterlab==4.* \
    notebook==7.* \
    ipywidgets==8.* \
    jupyterlab_widgets==3.* \
    numpy pandas matplotlib scikit-learn tensorflow==2.15.* pillow \
    tensorflow-datasets \
    fastapi uvicorn[standard]

WORKDIR /workspace
EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--ServerApp.token=", "--ServerApp.password=", "--allow-root"]