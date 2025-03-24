import cv2
image = cv2.imread('lol.jpg')

M = cv2.getRotationMatrix2D((0,0), 30, 1)
rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("After rotation", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()