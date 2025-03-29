import cv2

image = cv2.imread('littleBow.jpg')
cv2.imshow('image', image)

# horizontally & vertically
flipped = cv2.flip(image, -1)

cv2.imshow('flipped', flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
