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

img = cv.imread('I Love You.png', 1)
cv.imshow('original', img)
imgInfo = img.shape
height= imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]
# src 3 -> dst 3 (左上角, 左下角,右上角)
matSrc = np.float32([[0,0],[0,height-1],[width-1, 0]])
# 需要注意的是 行列 和 坐标 是不一致的
matDst = np.float32([[50,50],[100, height-50],[width-200,100]])

matAffine = cv.getAffineTransform(matSrc,matDst) #mat 1 src 2 dst 形成组合矩阵
dst = cv.warpAffine(img, matAffine,(height, width))
cv.imshow('affine',dst)
cv.waitKey(0)