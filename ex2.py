import numpy as np
import cv2

image1 = cv2.imread('huh.jpg')
image2 = cv2.imread('huhcopy.jpg')

cv2.imshow("Image 1", image1)
cv2.imshow("Image 1 rotated", image2)

bitwiseXOR = cv2.bitwise_xor(image1, image2)
cv2.imshow("Differences", bitwiseXOR)
cv2.waitKey(0)
cv2.destroyAllWindows()