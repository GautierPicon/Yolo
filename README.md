# YOLO

A CLI-based object detection system powered by [YOLOv8](https://docs.ultralytics.com/). Detect objects in real time through your webcam or run inference on static images from the terminal.

---

## Requirements

- Python ≥ 3.14
- [uv](https://docs.astral.sh/uv/)
- A webcam (for live detection mode)
- macOS with Apple Silicon (for MPS acceleration) — CPU fallback can be configured manually

---

## Installation

```bash
# Clone the repository
git clone https://codeberg.org/GautierPicon/Yolo
cd yolo

# Install dependencies with uv
uv sync
```

On first run, the YOLOv8s model weights (`yolov8s.pt`) will be downloaded automatically by Ultralytics.

---

## Usage

```bash
uv run main.py
```

You'll be presented with the interactive menu