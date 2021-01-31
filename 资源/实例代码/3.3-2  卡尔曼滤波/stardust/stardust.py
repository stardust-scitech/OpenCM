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
#导入绘图模块，定义别名为plt
import matplotlib.pyplot as plt
 
#创建画板
frame = np.zeros((800,800,3),np.uint8)

#构建卡尔曼运算参数容器
last_mes = current_mes = np.array((2,1),np.float32)
last_pre = current_pre = np.array((2,1),np.float32)
 
#捕捉鼠标移动并连线
def mousemove(event, x,y,s,p):
    global frame, current_mes, mes, last_mes, current_pre, last_pre
    last_pre = current_pre
    last_mes = current_mes
    current_mes = np.array([[np.float32(x)],[np.float32(y)]])
    kalman.correct(current_mes)
    current_pre = kalman.predict()
    lmx, lmy = last_mes[0],last_mes[1]
    lpx, lpy = last_pre[0],last_pre[1]
    cmx, cmy = current_mes[0],current_mes[1]    
    cpx, cpy = current_pre[0],current_pre[1]    
    cv.line(frame, (int(lmx),int(lmy)),(int(cmx),int(cmy)),(0,200,0))
    cv.line(frame, (int(lpx),int(lpy)),(int(cpx),int(cpy)),(0,0,200))
 
#对窗口命名
cv.namedWindow("Kalman")
#设置鼠标回调函数
cv.setMouseCallback("Kalman", mousemove)

#构造卡尔曼滤波器
kalman = cv.KalmanFilter(4,2)
#测量矩阵
kalman.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
#状态转移矩阵
kalman.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]], np.float32)
#系统误差
kalman.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], np.float32) * 0.003
#测量误差
kalman.measurementNoiseCov = np.array([[1,0],[0,1]], np.float32) * 1
 
while(True):
    #循环显示
    cv.imshow('Kalman',frame)
    #等待按键按下，退出循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
