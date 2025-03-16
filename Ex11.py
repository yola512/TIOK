import cv2
# ex.11
image10 = cv2.imread('sadeq.jpg', cv2.IMREAD_GRAYSCALE)
if image10 is None:
    print("ERROR: Could not read image")
    exit()
(h, w) = image10.shape

# brightest_pixel
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image10)
print(f"Brightest pixel location: {max_loc}")
print("Brightest pixel value: ", max_val)