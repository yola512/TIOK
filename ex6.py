import numpy as np
import cv2

image = cv2.imread('profilePic.jpg')

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv2.circle(image, (200, 200), 15, red)
cv2.circle(image, (230, 230), 15, red)
cv2.rectangle(image, (100, 100), (200, 200), green)
cv2.circle(image, (100, 100), 80, blue)

cv2.imshow("Profile picture", image)
cv2.waitKey()
cv2.destroyAllWindows()

# finish later