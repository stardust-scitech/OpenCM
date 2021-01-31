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
 
#构造参数序列
pos = np.array([
        [1, 1],
        [2, 4.2], 
        [3, 9.3],        
        [4, 16.4],     
        [5, 25.5]], np.float32)    
 
#构造二维卡尔曼滤波器
kalman = cv.KalmanFilter(2,2)

#测量矩阵
kalman.measurementMatrix = np.array([[1,0],[0,1]],np.float32)
#状态转移矩阵
kalman.transitionMatrix = np.array([[1,0],[0,1]], np.float32)
#系统误差
kalman.processNoiseCov = np.array([[1,0],[0,1]], np.float32) *1e-1
#测量误差
kalman.measurementNoiseCov = np.array([[1,0],[0,1]], np.float32) * 0.01
#预测值
kalman.statePre =  np.array([[6],[6]],np.float32)
 
for i in range(len(pos)):
    #重构矩阵
    mes = np.reshape(pos[i,:],(2,1))
    #原有参数修正
    x = kalman.correct(mes)
    #原有参数预测
    y = kalman.predict()
    #输出结果
    print(kalman.statePost[0],kalman.statePost[1])
    print(kalman.statePre[0],kalman.statePre[1])
    print("Measurement:\t",mes[0],mes[1])  
    print("Correct:\t",x[0],x[1])
    print("Predict:\t",y[0],y[1])     
    print("="*30)