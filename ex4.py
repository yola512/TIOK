import cv2
import imutils
image = cv2.imread('hamster.jpg')

cv2.imshow('Original image', image)

methods = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]

for method in methods:
    resized = imutils.resize(image, width=image.shape[1] * 3, inter = method)
    cv2.imshow('Resized image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()