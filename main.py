import cv2

# ex.1
image = cv2.imread('vangogh.jpg')

cv2.imshow("Displaying image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ex.2
image1 = cv2.imread('vangogh.jpg')
if image1 is None:
    print("Obraz nie zostal poprawnie wczytany")
else:
    (h, w, c) = image1.shape
    print(f'Channels: {c}')

# ex.3
image2 = cv2.imread('vangogh.jpg', cv2.IMREAD_GRAYSCALE)
if image2 is None:
    print("Obraz nie zostal poprawnie wczytany")
else:
    (h, w) = image2.shape
    c = 1 ## w grayscale - obraz ma 1 kanal
    print(f'Channels: {c}')

# ex.4
greyVanGogh = cv2.imread('vangogh.jpg', cv2.IMREAD_GRAYSCALE)
if greyVanGogh is None:
    print("Obraz nie zostal poprawnie wczytany")
else:
    output = "/Users/yola/Downloads/greyVanGogh.jpg"
    cv2.imwrite(output, greyVanGogh)

cv2.imshow("Greyscale image", greyVanGogh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ex.5
greyVanGogh = cv2.imread('vangogh.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread('vangogh.jpg')

if greyVanGogh is None or image is None:
    print("Nie udalo sie wczytac jednego z obrazow")
cv2.imshow("GreyscaleImage", greyVanGogh)
cv2.imshow("VanGoghOriginal", image)

cv2.waitKey(0)
cv2.destroyWindow("GreyscaleImage")
cv2.destroyWindow("VanGoghOriginal")

# ex.6
image3 = cv2.imread('vangogh.jpg')

if image3 is None:
    print("Nie mozna wczytac obrazu")
else:
    cv2.namedWindow("Van Gogh", cv2.WINDOW_NORMAL)
    image_resized = cv2.resize(image3, (1920, 1080))
    cv2.imshow("Van Gogh", image_resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()