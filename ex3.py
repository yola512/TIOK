import cv2
import numpy as np

image = cv2.imread('car.jpg')
cv2.imshow("Original image", image)

# converting BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Red mask", red_mask)

result = cv2.bitwise_and(image, image, mask=red_mask)

cv2.imshow("Result", result)
cv2.waitKey(0)
