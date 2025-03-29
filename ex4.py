import cv2

image = cv2.imread('littleBow.jpg')
cv2.imshow('Original image', image)

# horizontally
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontally flipped image', flipped)

# vertically
flipped1 = cv2.flip(image, 0)
cv2.imshow('Vertically flipped image', flipped1)

# horizontally and vertically
flipped2 = cv2.flip(image, -1)
cv2.imshow('Horizontally & Vertically flipped image', flipped2)

cv2.waitKey(0)
cv2.destroyAllWindows()