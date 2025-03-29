import cv2

image = cv2.imread('littleBow.jpg')
cv2.imshow('Original image', image)

(h,w) = image.shape[:2]

# cut the right half
img = image[:h, w//2:]

# flipped the right half
flipped_img = cv2.flip(img, 1)

# paste flipped half to original image
image[:h, w//2:] = flipped_img

cv2.imshow('Changed image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
