import cv2
import imutils

image = cv2.imread('hamster.jpg')

resized = imutils.resize(image, width = image.shape[1]//5, inter=cv2.INTER_AREA)
resized1 = imutils.resize(image, width = image.shape[1]//5, inter=cv2.INTER_CUBIC)
#resized1 = imutils.resize(image, width = image.shape[1]//5, inter=cv2.INTER_LINEAR)
#resized1 = imutils.resize(image, width = image.shape[1]//5, inter=cv2.INTER_LANCZOS4)
#resized1 = imutils.resize(image, width = image.shape[1]//5, inter=cv2.INTER_NEAREST)

cv2.imshow('Resized image', resized)
cv2.imshow('Another image to compare', resized1)
cv2.waitKey(0)
cv2.destroyAllWindows()