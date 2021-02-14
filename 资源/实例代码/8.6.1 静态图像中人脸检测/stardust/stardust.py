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

img = cv2.imread('ai.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
faces = face_cascade.detectMultiScale(gray,1.3,5)
    
for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
    
cv2.namedWindow('Person Detected!')
cv2.imshow('Person Detected!',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
