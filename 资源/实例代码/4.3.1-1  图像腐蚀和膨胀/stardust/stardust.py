#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_03
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

img = cv.imread('HelloWorld.png')
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
#创建结构单元
kernel=cv.getStructuringElement(cv.MORPH_RECT,(9,9))
#开运算
img_open=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
#显示彩色图像
cv.imshow("Color image",img)
#显示处理后图像
cv.imshow("Erosion image",erosion)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
