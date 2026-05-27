import os
import subprocess
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

try:
    from pi_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".tif", ".gif", ".heic", ".heif"}


def _load_image(image_path: str) -> np.ndarray | None:
    ext = os.path.splitext(image_path)[1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        print(f"Unsupported format: {ext}  (supported: {', '.join(SUPPORTED_EXTENSIONS)})")
        return None
    try:
        pil_img = Image.open(image_path).convert("RGB")
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    except Exception as e:
        print(f"Failed to read image: {e}")
        return None


def _open_in_finder(path: str) -> None:
    subprocess.run(["open", "--reveal", path])


def run_image(image_path: str, model_path: str = "yolov8s.pt") -> None:
    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        return

    model = YOLO(model_path)

    frame = _load_image(image_path)
    if frame is None:
        return

    results = model(frame, device="mps", verbose=False)
    annotated = results[0].plot()

    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_detected{ext}"
    cv2.imwrite(output_path, annotated)

    print(f"Saved: {output_path}")
    _open_in_finder(output_path)