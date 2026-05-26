from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Unable to open the camera")
    exit()

print("Press Q to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(
        frame,
        device="mps",
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Camera", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()