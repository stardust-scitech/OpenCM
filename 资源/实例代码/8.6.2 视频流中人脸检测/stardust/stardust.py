#file stardust.py
#author 凡尘(Kevin Brooks)
#version 1.0
#date 2020_08_04
#github https://github.com/stardust-kevin
#copyright Copyright (C) 2016, Stardust Studio,  All Rights Reserved
#license http://www.apache.org/licenses/LICENSE-2.0

#导入基本功能cv2库
import cv2

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
    
camera = cv2.VideoCapture(0)
while(True):
    ret,frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    #检测人脸
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
    #检测眼睛
    eyes = eye_cascade.detectMultiScale(gray,1.3,5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
    cv2.imshow('camera',frame)
                
    if cv2.waitKey(1000//12) & 0xff == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
