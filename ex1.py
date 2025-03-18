import numpy as np
import cv2

image = cv2.imread('cutie.jpg')
cv2.imshow('kotek', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 30 w prawo, 40 w dol, macierz M i cv2.warpAffine
M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted  = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('shifted kotek', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
