import cv2

image = cv2.imread("huh.jpg")
image1 = cv2.imread("huhcopy.jpg")
if image is None:
    print("ERROR: Could not read image")
    exit()
if image1 is None:
    print("ERROR: Could not read image1")
    exit()

cv2.imshow('Original', image)
cv2.imshow('Rotated', image1)

# a bit different pic (rotated):
difference = cv2.absdiff(image, image1)

# identical pic: (it's all black)
# difference = cv2.absdiff(image, image)

cv2.imshow('Difference', difference)
cv2.waitKey(0)
cv2.destroyAllWindows()

