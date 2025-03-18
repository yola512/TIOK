import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = 'uint8')

# a)
blue = (255, 0, 0)
red = (0, 0, 255)
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.circle(canvas, (40,40), 40, blue)
cv2.circle(canvas, (centerX, centerY), 60, red)

cv2.imshow("Another one", canvas)
cv2.waitKey()
cv2.destroyAllWindows()
