#file      stardust.py
#author    OpenCV, https://docs.opencv.org/4.5.0/d7/d00/tutorial_meanshift.html
#version   
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright 
#license   

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#开启摄像头
cap = cv.VideoCapture(0)
#单帧捕捉
ret, frame = cap.read()
#初始化跟踪框
track_window = (frame.shape[0], frame.shape[0], frame.shape[0], frame.shape[0])
#BGR转HSV
hsv_roi =  cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#设置亮度阈值
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
#获取图像直方图
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
#归一化处理
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
#设置迭代次数为5，最多十次迭代
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 5, 1)

while(1):
    #单帧捕捉
    ret ,frame = cap.read()
    #判断是否存在图像
    if ret == True:
        #BGR转HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #特征提取
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        #进行目标追踪
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        #查找旋转矩形的四个顶点
        pts = cv.boxPoints(ret)
        #类型转换
        pts = np.int0(pts)
        #绘制矩形框
        img = cv.polylines(frame,[pts],True, 255,2)
        #显示合成图像
        cv.imshow("Cap image",img)
    #等待按下“Esc”键退出
    if cv.waitKey(1) == 27:
        break
