import cv2
import imutils

image = cv2.imread('lol.jpg')

rotated1 = imutils.rotate(image, 30)
rotated2 = imutils.rotate(image, 30)
rotated3 = imutils.rotate(image, 30)

rotated90 = imutils.rotate(image, 90)

cv2.imshow("After three rotates (3 x 30 degrees)", rotated3)
cv2.imshow("Rotated - 90 degress", rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()