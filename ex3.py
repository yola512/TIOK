import cv2
import numpy as np

image = cv2.imread('cutie.jpg')
(h, w) = image.shape[:2]

(halfH, halfW) = (h // 2, w // 2)
M = np.float32([[1, 0, halfW], (0, 1, halfH)])
shifted = cv2.warpAffine(image, M, (h, w))

cv2.imshow('shifted cutie', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()