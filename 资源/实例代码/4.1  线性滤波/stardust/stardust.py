#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库
import numpy

#加载图片
img=cv.imread("street.jpg")
#方框滤波
img_box=cv.boxFilter(img,-1,(3,3),normalize=True)
#显示彩色图像
cv.imshow("color image",img)
#显示处理后图像
cv.imshow("box image",img_box)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
