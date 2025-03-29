import cv2

image=cv2.imread('hamster.jpg')

cv2.imshow('Original image', image)

resized = cv2.resize(image, (200, 300))

cv2.imshow('Resized image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
