import cv2
import numpy as np

image = cv2.imread('bluecar.jpg')

cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 100, 100])
upper_blue = np.array([110, 255, 255])

lower_blue2 = np.array([111, 100, 100])
upper_blue2 = np.array([130, 255, 255])

mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
mask2 = cv2.inRange(hsv, lower_blue2, upper_blue2)

blue_mask = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Blue mask", blue_mask)

#result = cv2.bitwise_and(image, image, mask=blue_mask)
#cv2.imshow("Result", result)

h, s, v = cv2.split(hsv)

# saturation +85 (255/3)
s = cv2.add(s, blue_mask//3)
increased_saturation = cv2.merge([h, s, v])
increased_saturation = cv2.cvtColor(increased_saturation, cv2.COLOR_HSV2BGR)
cv2.imshow("Increased saturation", increased_saturation)

cv2.waitKey(0)