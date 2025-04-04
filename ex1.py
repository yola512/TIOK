import numpy as np
import cv2

image = cv2.imread('idk.jpg')

roi = image[0:100, 0:100]

cv2.imshow('Left upper corner', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()