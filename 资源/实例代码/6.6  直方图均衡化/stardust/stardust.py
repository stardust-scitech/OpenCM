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
 
img = cv.imread('cat.jpg')
img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
img_output = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
 
cv.imshow('Color input image', img)
cv.imshow('Histogram equalized', img_output)
 
cv.waitKey(0)
