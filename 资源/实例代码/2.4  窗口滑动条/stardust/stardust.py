#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_21
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#创建空函数
def void():
    pass
#生成画布
img = np.zeros((640,480,3), np.uint8)
#创建调整窗口
cv.namedWindow('bar')
#创建颜色滑动条
cv.createTrackbar('B','bar',0,255, void)
cv.createTrackbar('G','bar',0,255, void)
cv.createTrackbar('R','bar',0,255, void)
#创建开关
switch = 'OFF=0/ON=1'
cv.createTrackbar(switch, 'bar', 0, 1, void)
while(1):
    # 得到轨迹当前位置
    b = cv.getTrackbarPos('B','bar')
    g = cv.getTrackbarPos('G','bar')
    r = cv.getTrackbarPos('R','bar')
    s = cv.getTrackbarPos(switch,'bar')
    #判断滑动条类型并格式化图像数组
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
    #显示处理图像
    cv.imshow('image', img)
    #等待退出按键按下
    if cv.waitKey(1) == ord('r'): 
        break
