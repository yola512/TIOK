import cv2
# ex.9
image8 = cv2.imread('sadeq.jpg')
if image8 is None:
    print("ERROR: Could not read image")
    exit()

cv2.imshow('Before', image8)
image8[50:100, 50:100] = (255,255,255)
cv2.imshow('After', image8)

cv2.waitKey(0)
cv2.destroyAllWindows()