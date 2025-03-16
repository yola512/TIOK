import cv2
# ex.2
image1 = cv2.imread('sadeq.jpg')
if image1 is None:
    print("ERROR: Could not read image")
    exit()
(h,w) = image1.shape[:2]
cv2.imshow("Cutie", image1)
(b,g,r) = image1[h-1, w-1]
print("Pixel at the bottom-right corner before - Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))

image1[h-1, w-1] = (0, 0, 255)
cv2.imshow("Pixel at the bottom-right corner set to red", image1)
(b,g,r) = image1[h-1, w-1]
print("Pixel at the bottom-right corner after - Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))

cv2.waitKey(0)
cv2.destroyAllWindows()
