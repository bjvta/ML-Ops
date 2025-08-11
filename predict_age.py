#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image


def load_model(model_path: Path) -> tf.keras.Model:
    if not model_path.exists():
        sys.stderr.write(f"[ERROR] No se encontró el modelo en: {model_path}\n")
        sys.exit(1)
    try:
        model = tf.keras.models.load_model(str(model_path))
        return model
    except Exception as e:
        sys.stderr.write(f"[ERROR] No se pudo cargar el modelo: {e}\n")
        sys.exit(1)


def preprocess_image(image_path: Path, img_size: int) -> np.ndarray:
    if not image_path.exists():
        sys.stderr.write(f"[ERROR] No se encontró la imagen: {image_path}\n")
        sys.exit(1)
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        sys.stderr.write(f"[ERROR] No se pudo abrir la imagen: {e}\n")
        sys.exit(1)

    img = img.resize((img_size, img_size))
    arr = np.array(img, dtype=np.float32) / 255.0  # normalización 0-1
    arr = np.expand_dims(arr, axis=0)  # (1, H, W, 3)
    return arr


def main():
    parser = argparse.ArgumentParser(
        description="Predicción de edad con modelo CNN entrenado en UTKFace."
    )
    parser.add_argument(
        "--model",
        default="models/utkface_age",
        help="Ruta al directorio SavedModel (por defecto: models/utkface_age)",
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Ruta al archivo .jpg/.png con el rostro",
    )
    parser.add_argument(
        "--img-size",
        type=int,
        default=128,
        help="Tamaño de entrada del modelo (por defecto: 128)",
    )
    args = parser.parse_args()

    model_path = Path(args.model)
    image_path = Path(args.image)

    model = load_model(model_path)
    x = preprocess_image(image_path, args.img_size)

    try:
        y_pred = float(model.predict(x, verbose=0).ravel()[0])
    except Exception as e:
        sys.stderr.write(f"[ERROR] Falla durante la inferencia: {e}\n")
        sys.exit(1)

    # Redondeo “amigable” (una cifra decimal)
    print(f"Edad estimada: {y_pred:.1f} años")


if __name__ == "__main__":
    main()

# Para ejecutarlo
# docker exec -it tf-lab bash