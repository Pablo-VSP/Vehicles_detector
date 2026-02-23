class ObjectCounter:
    def __init__(self, line_y):
        self.line_y = line_y
        self.counted_ids = set()
        self.class_counts = {}

    def update(self, boxes, ids, classes, model_names):
        for box, obj_id, cls in zip(boxes, ids, classes):
            x1, y1, x2, y2 = box
            center_y = int((y1 + y2) / 2)

            if center_y > self.line_y and obj_id not in self.counted_ids:
                self.counted_ids.add(obj_id)

                class_name = model_names[int(cls)]
                self.class_counts[class_name] = \
                    self.class_counts.get(class_name, 0) + 1

    def get_counts(self):
        return self.class_counts