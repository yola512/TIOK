import cv2
import imutils

image = cv2.imread("lol.jpg")

# warpAffine
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1)
rotatedWA = cv2.warpAffine(image, M, (w, h))

# imutils_rotate
rotatedIR = imutils.rotate(image, 60)

cv2.imshow("Rotation with warpAffine", rotatedWA)
cv2.imshow("Rotation with imutils_rotate", rotatedIR)
cv2.waitKey(0)
cv2.destroyAllWindows()