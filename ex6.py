import cv2
import imutils

image = cv2.imread('lol.jpg')
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("After rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
