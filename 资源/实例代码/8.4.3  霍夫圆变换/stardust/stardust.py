#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#载入图片
img = cv.imread("circle.jpg")
#BGR转灰度
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#中值滤波
gray = cv.medianBlur(gray,5)
#霍夫圆变换
circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=140,maxRadius=160)
#转化整数
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    #画圆轮廓
    cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    #画中心点
    cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
#显示处理后的图像
cv.imshow("Detected circles",img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
