import cv2
from ultralytics import YOLO


def run_webcam(model_path: str = "yolov8s.pt") -> None:
    model = YOLO(model_path)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Cannot open camera.")
        return

    print("Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, device="mps", verbose=False)
        annotated = results[0].plot()
        cv2.imshow("YOLO — Webcam", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()