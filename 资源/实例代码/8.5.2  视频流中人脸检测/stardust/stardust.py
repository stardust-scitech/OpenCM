#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_19
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv

#导入级联分类器训练结果
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
#导入级联分类器训练结果
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
#开启电脑摄像头
cap = cv.VideoCapture(0)

while 1:
    #单帧捕捉
    ret, frame = cap.read()
    #BGR转灰度
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #基于训练结果进行人脸识别
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    #框选出所有人脸
    for(x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 4)
    #基于训练结果进行眼睛识别
    eyes = eye_cascade.detectMultiScale(gray, 1.5, 6)
    #框选出所有眼睛
    for (e_x, e_y, e_w, e_h) in eyes:
        cv.rectangle(frame, (e_x, e_y),(e_x+e_w, e_y+e_h),(0,255,0), 4)       
    #显示处理后的图像
    cv.imshow("Face detection image",frame)
    #等待按下“Esc”键退出
    if cv.waitKey(1) == 27:
        break
