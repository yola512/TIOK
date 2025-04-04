import cv2

image = cv2.imread('idk.jpg')

cropped = image[0:300, 0:300]
cv2.imwrite('cropped_image.jpg', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
