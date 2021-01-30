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

#鼠标控制标志位
MoveFlag = 0

#鼠标回调函数
def draw_circle(event,x,y,flags,param):
    #声明全局变量
    global MoveFlag

    #鼠标按下
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),2,(255,0,0),-1)
        MoveFlag = 1
    #鼠标移动
    if event==cv.EVENT_MOUSEMOVE and MoveFlag==1:
        cv.circle(img,(x,y),2,(255,0,0),-1)
    #鼠标抬起
    if event==cv.EVENT_LBUTTONUP and MoveFlag==1:
        MoveFlag = 0

#创建画布
img = np.zeros((480,640,3),np.uint8)
#创建绘图窗口
cv.namedWindow('image')
#创建鼠标回调事件
cv.setMouseCallback('image',draw_circle)
 
while(1):
    #显示处理图像
    cv.imshow('image', img)
    #等待退出按键按下
    if cv.waitKey(1) == ord('r'): 
        break
