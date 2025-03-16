import cv2
# ex.3
image2 = cv2.imread('sadeq.jpg')
if image2 is None:
    print("ERROR: Could not read image")
    exit()
(h,w) = image2.shape[:2]
cv2.imshow(':)', image2)

# center of the image
(cX, cY) = (w // 2, h // 2)
print("Image center coordinates: ({0},{1})".format(cX, cY))
(b,g,r) = image2[cX, cY]
print("Image color: (rgb) ({0},{1},{2})".format(r,g,b))

cv2.waitKey(0)
cv2.destroyAllWindows()