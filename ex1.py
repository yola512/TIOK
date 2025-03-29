import cv2

image = cv2.imread('hamster.jpg')
cv2.imshow('Original image', image)

(h,w) = image.shape[:2]
resized = cv2.resize(image, (int(0.5*w), int(0.5*h)))

cv2.imshow('Resized image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()