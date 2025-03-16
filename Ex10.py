import cv2
# ex.10
image9 = cv2.imread("sadeq.jpg")
if image9 is None:
    print("ERROR: Could not read image")
    exit()
(h,w) = image9.shape[:2]

(b,g,r) = image9[50, 50]
print("Pixel at (50,50) - Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))
(b1,g1,r1) = image9[200, 200]
print("Pixel at (200,200) - Red: {0}, Green: {1}, Blue: {2}".format(r1,g1,b1))
