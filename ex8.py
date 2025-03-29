import cv2
import imutils

image = cv2.imread('hamster.jpg')

resized = imutils.resize(image, width = image.shape[1] * 4, inter=cv2.INTER_CUBIC)
resized1 = imutils.resize(image, width = image.shape[1] * 4, inter=cv2.INTER_LANCZOS4)

cv2.imshow('Resized using INTER_CUBIC', resized)
cv2.imshow('Resized using INTER_LANCZOS4', resized1)
cv2.waitKey(0)
cv2.destroyAllWindows()