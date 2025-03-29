import cv2
import imutils
import numpy as np

image = cv2.imread('hamster.jpg')

(h, w) = image.shape[:2]
for i in np.arange(1.0, 3.2, 0.2):
    resized = imutils.resize(image, width = int(w * i))
    cv2.imshow('Resized image', resized)
    cv2.waitKey(500)
cv2.destroyAllWindows()