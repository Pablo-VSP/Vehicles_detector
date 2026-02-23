from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path="yolov8s.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame, classes=None):
        results = self.model.track(
            frame,
            persist=True,
            classes=classes
        )
        return results