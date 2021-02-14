#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv

img = cv.imread('I Love You.png', 1)
cv.imshow('original', img)
imgInfo = img.shape
height= imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]

# 定义一个旋转矩阵
matRotate = cv.getRotationMatrix2D((height*0.5, width*0.5), 30, 0.7) # mat rotate 1 center 2 angle 3 缩放系数

dst = cv.warpAffine(img, matRotate, (height, width))

cv.imshow('rotate',dst)
cv.waitKey(0)
