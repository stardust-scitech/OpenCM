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

img = cv.imread('workshop.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
edges = cv.Canny(gray,50,150,apertureSize = 3) 
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10) 
for line in lines: 
    x1,y1,x2,y2 = line[0] 
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2) 
cv.imshow("HelloWorld image",img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
