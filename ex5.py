import cv2
import imutils

image = cv2.imread('cutie.jpg')

tx = input("Enter shift value tx: ")
ty = input("Enter shift value ty: ")

shifted = imutils.translate(image, tx, ty)
cv2.imshow('shifted cutie', shifted)
cv2.waitKey(0)
