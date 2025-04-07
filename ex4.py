import cv2

image = cv2.imread("huh.jpg")
if image is None:
    print("ERROR: Could not read image")
    exit()

cv2.imshow('Original', image)

(b, g, r) = cv2.split(image)

r = cv2.add(r, 30)
g = cv2.subtract(g, 20)
b = cv2.add(b, 10)

changedImage = cv2.merge([b, g, r])

cv2.imshow('My own filter', changedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

