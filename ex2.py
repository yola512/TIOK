import cv2
import numpy as np

image = cv2.imread('cutie.jpg')
M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('shifted cutie', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
