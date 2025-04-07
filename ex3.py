import numpy as np
import cv2

image = cv2.imread('huh.jpg')

if image is None:
    print("ERROR: Could not read image")
    exit()

cv2.imshow('Original', image)

M = np.ones(image.shape, dtype="uint8") * 80

subtracted = cv2.subtract(image, M)
subtracted1 = np.uint8(image) - np.uint8(M)

cv2.imshow('Darker in openCV', subtracted)
cv2.imshow("Darker in numpy", subtracted1)
cv2.waitKey(0)
cv2.destroyAllWindows()

