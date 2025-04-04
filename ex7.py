import cv2

image = cv2.imread('idk.jpg')

(h, w) = image.shape[:2]

# upper row
upper_left = image[0:h//3, 0:w//3]
upper_middle = image[0:h//3, w//3:2*w//3]
upper_right = image[0:h//3, 2*w//3:w]

# middle row
middle_left = image[h//3:2*h//3, 0:w//3]
center = image[h//3:2*h//3, w//3:2*w//3]
middle_right = image[h//3:2*h//3, 2*w//3:w]

# lower row
lower_left = image[2*h//3:h, 0:w//3]
lower_middle = image[2*h//3:h, w//3:2*w//3]
lower_right = image[2*h//3:h, 2*w//3:w]

cv2.imshow('upper left', upper_left)
cv2.imshow('upper middle', upper_middle)
cv2.imshow('upper right', upper_right)

cv2.imshow('middle left', middle_left)
cv2.imshow('center', center)
cv2.imshow('middle right', middle_right)

cv2.imshow('lower left', lower_left)
cv2.imshow('lower middle', lower_middle)
cv2.imshow('lower right', lower_right)
cv2.waitKey(0)
cv2.destroyAllWindows()