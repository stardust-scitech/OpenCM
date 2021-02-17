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
 
#加载图片
img = cv.imread("cat.jpg")
#BGR转YUV格式
img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
#直方图均衡化
img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
#YUV转BGR格式
container = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
#显示原图
cv.imshow("Original image", img)
#显示直方图均衡化后的图像
cv.imshow("Histogram equalized", container)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
