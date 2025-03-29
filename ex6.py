import cv2
import imutils

image = cv2.imread('hamster.jpg')

cv2.imshow('Original image', image)

resized = imutils.resize(image, height=400)

cv2.imshow('Resized image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()