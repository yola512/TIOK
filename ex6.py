import cv2

image = cv2.imread('idk.jpg')

(h,w) = image.shape[:2]
(centerY, centerX) = (h//2, w//2)

# crop 100x100 piece
cropped = image[0:100, 0:100].copy()

# paste to the centre of the image
image[centerY-50:centerY+50, centerX-50:centerX+50] = cropped

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()