import cv2

image = cv2.imread('idk.jpg')

(h,w) = image.shape[:2]
upper_half = image[0:h//2, 0:w]
lower_half = image[h//2:h, :w]

cv2.imshow('Lower half', lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()