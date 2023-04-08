import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # for (x , y, w, h) in faces:
    #     cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)
    left = []
    right = []
    if len(eyes) > 1:
        if eyes[0][0] > eyes[1][0]:
            left = eyes[1]
            right = eyes[0]
        else:
            left = eyes[0]
            right = eyes[1]

        for (x , y, w, h) in [left]:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
        for (x , y, w, h) in [right]:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        right_center = (right[0] + right[2] // 2 , right[1] + right[3] // 2)
        left_center = (left[0] + left[2] // 2, left[1] + left[3] // 2)
        cv.circle(frame ,right_center , radius = 5  , color = (255,0,0),thickness = -1)
        cv.circle(frame ,left_center , radius = 5  , color = (255,0,255),thickness = -1)

        angle = np.degrees(np.arctan((right_center[1] - left_center[1])/ (right_center[0] - left_center[0])))
        print("Tilt Angle: " + str(angle) + " Degrees")

    cv.imshow('Frame',frame)
    if cv.waitKey(1) & 0xFF == 27:
        break
capture.release()
cv.destroyAllWindows()