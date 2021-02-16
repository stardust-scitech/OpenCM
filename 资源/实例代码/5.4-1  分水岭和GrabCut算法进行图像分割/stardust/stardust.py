#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_10_31
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#加载图片
img = cv.imread("HelloWorld.png")
#BGR转灰度
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#二值化
ret,thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
#创建结构单元
kernel = np.ones((3,3),np.uint8)
#图像膨胀
back_ground = cv.dilate(thresh,kernel,iterations=2)
#进行距离变换
distance_transform = cv.distanceTransform(thresh,cv.DIST_L2,5)
#阈值调节
ret,fore_ground = cv.threshold(distance_transform,0.3*distance_transform.max(),255,0)
#浮点转整数
fore_ground = np.uint8(fore_ground)
#两图像相减，获得重叠区域
unknown = cv.subtract(back_ground,fore_ground) 
#连通域标记图像
ret,markers = cv.connectedComponents(back_ground)
#背景区域+1
markers = markers +1 
#非标记区域置0
markers[unknown==255] = 0
#漫水处理
markers = cv.watershed(img,markers)
#边界标记
img[markers == -1] = [0, 0, 255]
#显示处理后的图像
cv.imshow('Water image',img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
