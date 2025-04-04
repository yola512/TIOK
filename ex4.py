import cv2

image = cv2.imread('idk.jpg')

(h,w) = image.shape[:2]
print(h,w)
startX = int(input("Enter start X value: "))
endX = int(input("Enter end X value: "))
startY = int(input("Enter start Y value: "))
endY = int(input("Enter end Y value: "))

if startX < 0 or startX > w or endX < 0 or endX > w:
    print("\nERROR: StartX or endX outside the image boundaries")
if startY < 0 or startY > h or endY < 0 or endY > h:
    print("\nERROR: StartY or endY outside the image boundaries")

roi = image[startY:endY, startX:endX]

cv2.imshow('Output', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

