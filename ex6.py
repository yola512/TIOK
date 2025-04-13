import cv2
import numpy as np

image = cv2.imread('logo.png')
cv2.imshow('Original', image)

(B, G, R) = cv2.split(image)

# change blue with red
changed = cv2.merge((R, G, B))
cv2.imshow('Swapped blue and red channel', changed)

# get rid of red channel completely
zeroR = np.zeros_like(R)
noRed = cv2.merge((B, G, zeroR))
cv2.imshow('No red channel', noRed)

cv2.waitKey(0)