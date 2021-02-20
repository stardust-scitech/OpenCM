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
lines = cv.HoughLines(edges,1,np.pi/180,100)

for line in lines:
    #获得直线的截距和夹角
    rho,theta = line[0]
    #求取直线两端点坐标
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    #两点连线
    cv.line(img,(x1,y1),(x2,y2),(255,0,0),2)
#显示处理后的图像
cv.imshow("Hough image",img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
