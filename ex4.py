import cv2
import imutils

image = cv2.imread('cutie.jpg')
shifted = imutils.translate(image, 100, 50)
cv2.imshow('shifted kotek', shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()


