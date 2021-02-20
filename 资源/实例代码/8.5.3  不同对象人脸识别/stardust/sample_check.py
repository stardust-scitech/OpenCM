#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_19
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np
#导入操作系统模块
import os

#读取样本文件函数
def read_images(file_path):
    #构建列表
    x, y, z = [], [], []
    #读取待识别对象名称列表
    image_name_list = os.listdir(file_path)
    #将名称写入列表
    z = image_name_list
    #初始化标签计数器
    label = 0
    #读取待识别对象名称路径
    image_name_path = [file_path + i for i in image_name_list]
    for path in image_name_path:
        #获取图像列表
        images = os.listdir(path)
        for file in images:
            #读取每个样本文件
            img = cv.imread(path + "/" + file, 0)
            #将图像写入列表
            x.append(img)
            #将标签写入列表
            y.append(label)
        #标签计数器累加
        label += 1
    #转换为array类型
    y = np.array(y)
    return x, y, z

def check_sample(file_path):
    #读取采集到的样本
    x, y, z = read_images(file_path)
    #创建分类器
    model = cv.face.EigenFaceRecognizer_create()
    #训练模型
    model.train(x, y)
    #导入级联分类器训练结果
    face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    #开启电脑摄像头
    cap = cv.VideoCapture(0)

    while 1:
        #单帧捕捉
        ret, frame = cap.read()
        #BGR转灰度
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #基于训练结果进行人脸识别
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        #框选出所有人脸
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 4)
            #重构框选出的人脸图片
            frame_face = cv.resize(gray[y: y+h, x:x+w], (200, 200))
            #对模型进行预测
            params = model.predict(frame_face)
            #输出识别结果
            print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
            #标记人脸的名字
            if int(params[1])<5000:
                cv.putText(frame, z[params[0]], (x, y - 20), cv.FONT_HERSHEY_SIMPLEX, w/80, 255, int(w/30))
        #显示处理后的图像
        cv.imshow("Captured image", frame)
        #等待按下“Esc”键退出
        if cv.waitKey(10) == 27:
            break
