import cv2
# ex.4
image3 = cv2.imread('sadeq.jpg')

if image3 is None:
    print("ERROR: Could not read image")
    exit()
(h,w) = image3.shape[:2]

print("Image coordinates:")
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
if not (0 <= x < w and 0 <= y < h):
    print("ERROR: Coordinates out of range")
    exit()
else:
    image3[y,x] = [0,0,0]
    cv2.imshow("Selected pixel changed to black", image3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()