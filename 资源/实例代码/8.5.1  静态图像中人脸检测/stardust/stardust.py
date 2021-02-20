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
#载入人工合成的人脸
img = cv.imread("ai.jpg")
#BGR转灰度
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#基于训练结果进行人脸识别
faces = face_cascade.detectMultiScale(gray,1.1,3)

#框选出所有人脸
for (x,y,w,h) in faces:
    img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 4)

#显示处理后的图像
cv.imshow("Face detection image",img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
