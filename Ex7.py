import cv2
# ex.7
image6 = cv2.imread('sadeq.jpg')
if image6 is None:
    print("ERROR: Could not read image")
    exit()
cv2.imshow('Before', image6)
(h,w) = image6.shape[:2]
# centre of image
(cX, cY) = (w // 2, h // 2)
# 3 columns x 3 rows
(x, y) = (w // 3, h // 3)
print(x,y)

# top
tr = image6[0:y, 2*x:w]
tc = image6[0:y, x:2*x]
tl = image6[0:y, 0:x]

# middle
mr = image6[y:2*y, 2*x:w]
mc = image6[y:2*y, x:2*x]
cv2.imshow("Middle-Centre Corner", mc)
ml = image6[y:2*y, 0:x]

# bottom
br = image6[2*y:h, 2*x:w]
bc = image6[2*y:h, x:2*x]
bl = image6[2*y:h, 0:x]
print(x, y)

cv2.waitKey(0)
cv2.destroyAllWindows()