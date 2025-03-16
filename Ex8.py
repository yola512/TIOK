import cv2
# ex.8
image7 = cv2.imread('sadeq.jpg')
if image7 is None:
    print("ERROR: Could not read image")
    exit()
(h,w) = image7.shape[:2]

for row in range(h):
    if row == 100:
        image7[row] = (0,255,0)

cv2.imshow('changed 100th row', image7)
cv2.waitKey(0)
cv2.destroyAllWindows()
