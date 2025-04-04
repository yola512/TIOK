import cv2

image = cv2.imread('idk.jpg')

(h,w) = image.shape[:2]
right_half = image[0:h, w//2:w]

cv2.imshow('Right half', right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()