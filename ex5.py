import cv2
import imutils

image = cv2.imread('hamster.jpg')
cv2.imshow('Original image', image)

# width=500, keeping the proportions
resized = imutils.resize(image, width=500)
cv2.imshow('Resized image', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()