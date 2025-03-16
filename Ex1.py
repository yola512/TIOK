import cv2
# ex.1
image = cv2.imread('sadeq.jpg')
if image is None:
    print("ERROR: Could not read image")
    exit()
(h,w) = image.shape[:2]
cv2.imshow("Cutie", image)
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))
cv2.waitKey(0)
cv2.destroyAllWindows()