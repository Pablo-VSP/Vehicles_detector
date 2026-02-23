import cv2
import numpy as np

class LaneDetector:
    def detect(self, frame):
        height, width = frame.shape[:2]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)

        mask = np.zeros_like(edges)
        polygon = np.array([[
            (0, height),
            (width, height),
            (width//2, int(height*0.6))
        ]], np.int32)

        cv2.fillPoly(mask, polygon, 255)
        masked_edges = cv2.bitwise_and(edges, mask)

        lines = cv2.HoughLinesP(
            masked_edges, 2, np.pi/180,
            threshold=100,
            minLineLength=50,
            maxLineGap=50
        )

        line_image = np.zeros_like(frame)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

        return cv2.addWeighted(frame, 0.8, line_image, 1, 1)
