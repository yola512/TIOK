import cv2

image = cv2.imread('flower.jpg')

cv2.imshow('image', image)

(B, G, R) = cv2.split(image)

cv2.imshow('Red', R)
cv2.imshow('Green', G)
cv2.imshow('Blue', B)

cv2.waitKey(0)