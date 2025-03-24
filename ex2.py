import cv2

image = cv2.imread('lol.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Result", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()