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
img = cv.imread("I Love You.png")
#获取图片信息
info = img.shape
#获取图片纵向长度
height = info[0]
#获取图片横向长度
width = info[1]
#获取图片通道数
mode = info[2]

#创建原图3点(左上, 左下和右上)的坐标
matSrc = np.float32([[0,0],[0,height],[width, 0]])
#创建目标图像的3点坐标
matDst = np.float32([[0,0],[100, height-100],[width-100,100]])
#合并矩阵
matAffine = cv.getAffineTransform(matSrc,matDst) 
#进行仿射变换
container = cv.warpAffine(img, matAffine,(height, width))
#显示原图
cv.imshow("Original image", img)
#显示显示旋转后的图像
cv.imshow("Affine image", container)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
