#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_19
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入操作系统模块
import os

def take_sample(file_path, name, count_tar):
    #判断simple文件夹是否存在，不存在则创建simple文件夹
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    #判断simple文件夹是否存在，不存在则创建simple文件夹
    if not os.path.exists(file_path + name):
        os.makedirs(file_path + name)

    #导入级联分类器训练结果
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    #开启电脑摄像头
    cap = cv.VideoCapture(0)
    #捕捉成功次数计数器
    count_cur = 0

    while count_cur<count_tar:
        #单帧捕捉
        ret, frame = cap.read()
        #BGR转灰度
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #基于训练结果进行人脸识别
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #框选出所有人脸
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #重构框选出的人脸图片
            frame_face = cv.resize(gray[y: y+h, x:x+w], (200, 200))
            #显示处理后的图像
            cv.imshow("Captured image", frame_face)
            #重构框选出的人脸图片
            cv.imwrite(file_path+ name + "/%s.pgm" % str(count_cur), frame_face)
            #计数器累加
            count_cur += 1
        #等待按下“Esc”键退出
        if cv.waitKey(10) == 27:
            break
