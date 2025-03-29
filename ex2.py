import cv2
import imutils

image = cv2.imread('hamster.jpg')
cv2.imshow('Original image', image)
print('Original image size', image.shape[:2])

resized = imutils.resize(image, width=image.shape[1] * 2, inter = cv2.INTER_LINEAR)

cv2.imshow('Resized image', resized)
print('Resized image size', resized.shape[:2])
cv2.waitKey(0)
cv2.destroyAllWindows()