import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
green = (0, 255, 0)

for r in range(0, 160, 20):
    cv2.rectangle(canvas, (centerX + r, centerY + r), (centerX - r, centerY - r), green)

cv2.imshow("Square inside a square inside a sq-...", canvas)
cv2.waitKey()
cv2.destroyAllWindows()

