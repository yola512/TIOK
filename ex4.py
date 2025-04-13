import cv2

image = cv2.imread('flower.jpg')
cv2.imshow('Original', image)

(B, G, R) = cv2.split(image)

R = cv2.add(R, 200)

image2 = cv2.merge([B, G, R])

cv2.imshow('Increased R intensity', image2)
cv2.waitKey(0)