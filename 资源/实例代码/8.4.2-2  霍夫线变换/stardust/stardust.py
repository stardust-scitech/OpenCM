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
img = cv.imread("workshop.jpg")
#BGR转灰度
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#边缘检测
edges = cv.Canny(gray,50,150,apertureSize = 3) 
#检测到的边缘进行霍夫直线检测
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10) 

for line in lines: 
    #获得直线端点的横、纵坐标值
    x1,y1,x2,y2 = line[0] 
    #两点连线
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2) 
#显示处理后的图像
cv.imshow("Hough image",img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
