import cv2

image = cv2.imread('littleBow.jpg')
cv2.imshow('Little Bow', image)

print("How would you like to flip the image?")
print("Press '0' to flip vertically")
print("Press '1' to flip horizontally")
print("Press '-1' to flip both horizontally & vertically")
choice = input("\nPress '0' '1' or '-1': ")

flipped = cv2.flip(image, int(choice))

cv2.imshow('Flipped image', flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
