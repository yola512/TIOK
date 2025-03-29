import cv2
import imutils

image = cv2.imread('hamster.jpg')
cv2.imshow('Original', image)

resized = imutils.resize(image, width=800)
cv2.imwrite('resized_output.jpg', resized)

cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()