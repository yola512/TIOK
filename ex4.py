import cv2

image = cv2.imread('lol.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

angle = int(input("Enter the angle of rotation: "))
M = cv2.getRotationMatrix2D((cX, cY), angle, 1)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("After rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
