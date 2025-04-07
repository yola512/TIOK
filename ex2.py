import cv2
import numpy as np

image = cv2.imread('huh.jpg')

if image is None:
    print("ERROR: Could not read image")
    exit()

M = np.ones(image.shape, dtype = "uint8") * 150

added = np.uint8(image) + np.uint8(M)

added2 = cv2.add(image, M)

cv2.imshow('Original', image)
cv2.imshow('Added 150 to every pixel (numpy)', added)
cv2.imshow("Added 150 to every pixel (opencv)", added2)
cv2.waitKey(0)
cv2.destroyAllWindows()