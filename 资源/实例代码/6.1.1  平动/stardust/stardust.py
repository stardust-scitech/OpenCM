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

#定义x方向平移量
x_translation = 200

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
#创建空的图像容器
container = np.zeros(info, np.uint8)

for i in range( height ):
    for j in range( width - x_translation ):
        container[i, j + x_translation] = img[i, j]

#显示原图
cv.imshow("Original image", img)
#显示平移后的图像
cv.imshow("Translation image", container)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
