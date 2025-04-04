import cv2

image = cv2.imread('idk.jpg')

(h,w) = image.shape[:2]
for i in range(1, w, 10):
    changed = image[0:h, 0:i]
    cv2.imshow('mooooving', changed)
    cv2.waitKey(50)
    cv2.destroyAllWindows()
