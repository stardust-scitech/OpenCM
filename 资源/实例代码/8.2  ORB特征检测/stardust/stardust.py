#file stardust.py
#author 凡尘(Kevin Brooks)
#version 1.0
#date 2020_08_04
#github https://github.com/stardust-kevin
#copyright Copyright (C) 2016, Stardust Studio,  All Rights Reserved
#license http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np
#导入绘图模块，定义别名为plot
from matplotlib import pyplot as plot

#加载图片
img = cv.imread("board.jpg")
#初始化ORB
orb = cv.ORB_create()
#ORB检测
keypoints = orb.detect(img, None)
#绘制关键点
img = cv.drawKeypoints(img, keypoints, None, color=(255, 0, 0))
#绘制直方图
plot.imshow(img), plot.show()
