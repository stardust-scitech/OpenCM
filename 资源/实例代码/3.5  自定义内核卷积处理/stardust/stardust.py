#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_09_11
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#卷积核
average = np.array([
    [1/9, 1/9, 1/9],                       
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
                   ])

sharp = np.array([
    [ 0, -1,  0],                       
    [-1,  5, -1],
    [ 0, -1,  0]
                   ])

#self = np.array([
#    [0.058550/0.779484, 0.096532/0.779484, 0.058550/0.779484],                       
#    [0.096532/0.779484, 0.159155/0.779484, 0.096532/0.779484],
#    [0.058550/0.779484, 0.096532/0.779484, 0.058550/0.779484]
#                   ])
self = np.array([
    [0.058550, 0.096532, 0.058550],                       
    [0.096532, 0.159155, 0.096532],
    [0.058550, 0.096532, 0.058550]
                   ])

#加载图片
img = cv.imread("love.jpg")
#高斯模糊
gauss = cv.GaussianBlur(img,(3,3),0)
#卷均值处理
aver = cv.filter2D(img,-1,average) 
#锐化处理
shar = cv.filter2D(img,-1,sharp)
#自定义高斯模糊处理
user = cv.filter2D(img,-1,self)
#显示彩色图像
cv.imshow("image original", img)
#显示高斯模糊图像
cv.imshow("image gauss", gauss)
#显示均值处理后的图像
cv.imshow("image convolution", aver)
#显示锐化处理后的图像
cv.imshow("image sharp", shar)
#显示自定义高斯模糊处理后的图像
cv.imshow("image user", user)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)