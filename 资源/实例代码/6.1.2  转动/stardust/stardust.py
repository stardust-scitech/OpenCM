#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv

#定义旋转角度
z_rotate = 60

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

#定义一个旋转矩阵
matRotate = cv.getRotationMatrix2D((height*0.5, width*0.5), z_rotate, 0.7)
#进行仿射变换，一个维度变换的结果为产生旋转效果
container = cv.warpAffine(img, matRotate, (height, width))

#显示原图
cv.imshow("Original image", img)
#显示显示旋转后的图像
cv.imshow("Rotate image", container)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
