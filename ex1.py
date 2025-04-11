import cv2
import numpy as np

image = cv2.imread('lady.jpg')
cv2.imshow("Lady", image)

mask = np.zeros(image.shape[:2], dtype = 'uint8')
# rectangle
#cv2.rectangle(mask, (971, 824), (1983, 2130), 255, -1)
#cv2.imshow("Rectangular mask", mask)

# ellipse
cv2.ellipse(mask, (1457, 1472), (700, 700), 0, 0, 360, 255, -1)
cv2.imshow("Ellipse mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked image", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()