import cv2
import numpy as np

circle = np.zeros((300,300), dtype='uint8')
cv2.circle(circle, (150, 150), 100, 255, -1)

triangle = np.zeros((300,300), dtype='uint8')
pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
pts = pts.reshape((-1,1,2))
filledT = cv2.fillPoly(triangle,[pts], 255)

cv2.imshow("Triangle", filledT)
cv2.imshow("Circle", circle)

bitwiseOR = cv2.bitwise_or(triangle, circle)
bitwiseAND = cv2.bitwise_and(triangle, circle)
bitwiseXOR = cv2.bitwise_xor(triangle, circle)
bitwiseNOT = cv2.bitwise_not(triangle)

cv2.imshow("OR", bitwiseOR)
cv2.imshow("NOT (triangle)", bitwiseNOT)
cv2.imshow("XOR", bitwiseXOR)
cv2.imshow("AND", bitwiseAND)

cv2.waitKey(0)
cv2.destroyAllWindows()
