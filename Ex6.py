import cv2
# ex.6
image5 = cv2.imread('sadeq.jpg')
if image5 is None:
    print("ERROR: Could not read image")
    exit()
#cv2.imshow('Before', image5)
(h,w) = image5.shape[:2]

(cX, cY) = (w // 2, h // 2)
print(cX, cY)

image5[cY-50:cY+50, cX-50:cX+50] = (0,0,255)
cv2.imshow('After', image5)

cv2.waitKey(0)
cv2.destroyAllWindows()
