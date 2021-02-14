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

img = cv.imread("I Love You.png", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

dst = np.zeros(imgInfo, np.uint8)

for i in range( height ):
    for j in range( width - 100 ):
        dst[i, j + 100] = img[i, j]

cv.imshow('original', img)
cv.imshow('translation', dst)
cv.waitKey(0)
