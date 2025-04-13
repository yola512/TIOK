import cv2
import numpy as np
image = cv2.imread('flower.jpg')

(B, G, R) = cv2.split(image)

image2 = cv2.merge([R, G, B])

cv2.imshow("RGB", image2)

zeroG = np.zeros_like(R)

no_green = cv2.merge([B, zeroG, R])

cv2.imshow("Original", image)
cv2.imshow("No green", no_green)
cv2.waitKey(0)