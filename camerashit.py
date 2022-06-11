from cv2 import Canny
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()   

#img = cv2.imread('faces.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray,80,100)
    kernal = np.ones(1)
    erode = cv2.erode(edge, kernal, iterations=1)
    dilate = cv2.dilate(erode, kernal, iterations=2)

    faces = face_cascade.detectMultiScale(gray, 2, 4)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    cv2.imshow('dilate',dilate)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()