import cv2
import numpy as np

image = cv2.imread("lady.jpg")
cv2.imshow("Original image", image)

mask = np.zeros(image.shape[:2], dtype= 'uint8')
# rectangle mask
#cv2.rectangle(mask, (1123, 1300), (1346, 1381), 255, -1)
#cv2.rectangle(mask, (1589, 1300), (1791, 1391), 255, -1)

# ellipse mask
cv2.ellipse(mask, (1244, 1330), (100,100), 0, 0, 360, 255, -1)
cv2.ellipse(mask, (1700, 1371), (100,100), 0, 0, 360, 255, -1)

inverted_mask = cv2.bitwise_not(mask)
without_eyes = cv2.bitwise_and(image, image, mask = inverted_mask)

cv2.imshow("No eyes image", without_eyes)
cv2.waitKey(0)
cv2.destroyAllWindows()
