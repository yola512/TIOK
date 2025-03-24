import cv2
import imutils

image = cv2.imread("lol.jpg")

rotated = imutils.rotate(image, 75)
cv2.imwrite("rotated_output.jpg", rotated)