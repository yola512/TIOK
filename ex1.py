import cv2
import numpy as np

image = cv2.imread('huh.jpg')

if image is None:
    print("ERROR: Could not read image")
    exit()

cv2.imshow('Original', image)
# make brighter by 50
M = np.ones(image.shape, dtype="uint8") * 50

# cv2
added = cv2.add(image, M)

# numpy
added2 = np.uint8(image) + np.uint8(M)

cv2.imshow('Brighter using openCV', added)
cv2.imshow('vs in numPy', added2)
cv2.waitKey(0)
cv2.destroyAllWindows()