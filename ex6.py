import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')

image = cv2.imread('profilePic.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect face
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

for (x, y, w, h) in faces:
    # piece of the black&white image with detected face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    cv2.circle(roi_color, center=(h//2, w//2), radius=w//2, color=blue)

    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=1)
    for (ex, ey, ew, eh) in eyes[:2]:
        center = (x + ex + ew//2, y + ey + eh//2)
        cv2.circle(image, center, ew//2, red, -1)

    mouth = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.4)
    for (mx, my, mw, mh) in mouth:
        mouth_y = y + my + int(h * 0.4)
        mouth_x = x + mx - int(w * 0.15)
        # check if detected mouth is within the bounds of the face
        if mouth_y < y + h:
            cv2.rectangle(image, (mouth_x, mouth_y), (mouth_x+ mw, mouth_y + mh), green, -1)
            break


cv2.imshow("Profile picture", image)
cv2.waitKey()
cv2.destroyAllWindows()
