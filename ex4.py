from curses.textpad import rectangle

import numpy as np
import cv2

green = (0, 255, 0)
red = (255, 0, 0)

canvas = np.zeros((300, 300, 3), dtype="uint8")

(centerX, centerY) = canvas.shape[1] // 2, canvas.shape[0] // 2

cv2.rectangle(canvas, (90, 90), (210, 210), green)
cv2.circle(canvas, (centerX, centerY), 30, red)

cv2.imshow("Circle inside square", canvas)
cv2.waitKey()
cv2.destroyAllWindows()
