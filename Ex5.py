import cv2
# ex.5
image4 = cv2.imread('sadeq.jpg')
if image4 is None:
    print("ERROR: Could not read image")
    exit()
cv2.imshow('Before', image4)
(h,w) = image4.shape[:2]

(cX, cY) = (w // 2, h // 2)
tr = image4[0:cY, cX:w]
tl = image4[0:cY, 0:cX]
br = image4[cY:h, cX:w]
bl = image4[cY:h, 0:cX]

image4[0:cY, 0:cX] = (255,0,0)
cv2.imshow('After changing the top-left corner to blue', image4)

cv2.waitKey(0)
cv2.destroyAllWindows()