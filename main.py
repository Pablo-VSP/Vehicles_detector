# import cv2
# from app.detection.detector import ObjectDetector
# from app.counting.counter import ObjectCounter
# from app.lane.lane_detector import LaneDetector
# from app.config.settings import *

# from app.services.counter import count_objects
# from app.services.serializer import build_payload
# import json

# DEVICE_ID = "T2-SOM-001"
# LANE_ID = 1

# detector = ObjectDetector()
# counter = ObjectCounter(LINE_Y)
# lane_detector = LaneDetector()

# cap = cv2.VideoCapture(VIDEO_PATH)

# while True:
#     ret, frame = cap.read()
#     if not ret:

#         break
#     results = detector.detect(frame, TARGET_CLASSES)

#     if results[0].boxes.id is not None:
#         boxes = results[0].boxes.xyxy.cpu().numpy()
#         ids = results[0].boxes.id.cpu().numpy()
#         classes = results[0].boxes.cls.cpu().numpy()

#         counter.update(boxes, ids, classes, detector.model.names)

#         #Counter para el json de salida
#         counts = count_objects(results)
#         payload = build_payload(DEVICE_ID, LANE_ID, counts)
#         print(json.dumps(payload, indent=2))

#     # frame = lane_detector.detect(frame)

#     # cv2.imshow("Traffic AI", frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# ------------------------------------------------------------------------------------------
import cv2
import traceback
import json

print(">>> Iniciando programa...")

try:
    from app.detection.detector import ObjectDetector
    from app.counting.counter import ObjectCounter
    from app.lane.lane_detector import LaneDetector
    from app.config.settings import *
    from app.services.counter import count_objects
    from app.services.serializer import build_payload
    print(">>> Imports correctos")
except Exception as e:
    print("Error en imports:")
    traceback.print_exc()
    exit(1)


DEVICE_ID = "T2-SOM-001"
LANE_ID = 1

try:
    detector = ObjectDetector()
    print(">>> Detector inicializado")
except Exception as e:
    print("Error inicializando detector:")
    traceback.print_exc()
    exit(1)

try:
    counter = ObjectCounter(LINE_Y)
    print(">>> Counter inicializado")
except Exception as e:
    print("Error inicializando counter:")
    traceback.print_exc()
    exit(1)

try:
    lane_detector = LaneDetector()
    print(">>> Lane detector inicializado")
except Exception as e:
    print("Error inicializando lane detector:")
    traceback.print_exc()
    exit(1)


try:
    print(f">>> Intentando abrir video: {VIDEO_PATH}")
    cap = cv2.VideoCapture(VIDEO_PATH)
    
    if not cap.isOpened():
        raise Exception("No se pudo abrir el video/cámara")
    
    print(">>> VideoCapture abierto correctamente")

except Exception as e:
    print("Error abriendo VideoCapture:")
    traceback.print_exc()
    exit(1)


print(">>> Entrando al loop principal")

while True:
    try:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo leer frame. Fin o error de cámara.")
            break

        print(">>> Frame leído correctamente")

        results = detector.detect(frame, TARGET_CLASSES)
        print(">>> Detección ejecutada")

        if results and results[0].boxes.id is not None:

            boxes = results[0].boxes.xyxy.cpu().numpy()
            ids = results[0].boxes.id.cpu().numpy()
            classes = results[0].boxes.cls.cpu().numpy()

            print(">>> Boxes procesadas")

            counter.update(boxes, ids, classes, detector.model.names)
            print(">>> Counter actualizado")

            counts = count_objects(results)
            payload = build_payload(DEVICE_ID, LANE_ID, counts)

            print(">>> Payload generado:")
            print(json.dumps(payload, indent=2))

    except Exception as e:
        print("Error dentro del loop principal:")
        traceback.print_exc()
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print(">>> Salida manual")
        break


print(">>> Liberando recursos")
cap.release()
cv2.destroyAllWindows()
print(">>> Programa finalizado")