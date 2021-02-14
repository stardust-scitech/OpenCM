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

img = cv.imread("I Love You.png")
cv.imshow('original', img)
imgInfo = img.shape
height= imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

dst = np.zeros([height*2, width, deep], np.uint8)

for i in range( height ):
    for j in range( width ):
        dst[i,j] = img[i,j]
        dst[height*2-i-1,j] = img[i,j]

for i in range(width):
    dst[height, i] = (0, 0, 255)
cv.imshow('image', dst)
cv.waitKey(0)
