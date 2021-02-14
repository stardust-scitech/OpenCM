#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_10_31
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv

#加载图片
img = cv.imread("HelloWorld.png")  
#BGR转灰度
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  
#灰度图像二值化
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)  
#轮廓提取
contours, hierarchy = cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)  
#画出图像轮廓
cv.drawContours(img,contours,-1,(255,0,0),3)  
#显示合成后图像
cv.imshow("img", img)  
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
