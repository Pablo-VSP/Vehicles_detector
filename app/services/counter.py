from collections import defaultdict

# Mapeo COCO
CLASS_MAP = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
}

TARGET_CLASS_IDS = list(CLASS_MAP.keys())


def count_objects(results):
    counts = defaultdict(int)
    counts = {v: 0 for v in CLASS_MAP.values()}

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            if cls_id in CLASS_MAP:
                label = CLASS_MAP[cls_id]
                counts[label] += 1

    return dict(counts)