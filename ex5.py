import cv2

image = cv2.imread('face.jpg')
(h,w) = image.shape[:2]

upper_half = image[0:h//2, 0:w]
(h1,w1) = upper_half.shape[:2]

face_only = upper_half[50:h//2, w1//3:2*w//3]

cv2.imshow('Face only', face_only)
cv2.waitKey(0)
cv2.destroyAllWindows()