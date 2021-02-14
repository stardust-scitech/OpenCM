#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_05
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入绘图模块，定义别名为plot
from matplotlib import pyplot as plot

def EdgeDetection(img, t1, t2):
    #BGR(OpenCV使用BGR而非RGB格式)转灰度图像  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    #图像转为一维数组并获得灰度直方图以便调整算法的使用
    plot.hist(gray.ravel(), 256, [0, 256])
    #显示直方图窗口
    plot.show()
    #历遍每个像素元素并进行灰度处理
    for i in range(len(gray)):
        for j in range(len(gray[0])):
            if gray[i][j]>=t1 and gray[i][j]<=t2:
                gray[i][j] = 255
            else:
                gray[i][j] = 0
    gray_last = gray
    cv.imshow("EdgeDetection_Pre", gray)
    #历遍每个像素元素并进行二值化边缘处理
    for i in range(len(gray)):
        for j in range(len(gray[0])-3):
            if gray[i][j]==255 and gray[i][j+1]==0 and gray[i][j+2]==0:
                gray_last[i][j] = 255
            elif gray[i][j]==0 and gray[i][j+1]==255 and gray[i][j+2]==0:
                gray_last[i][j] = 255
            elif gray[i][j]==0 and gray[i][j+1]==0 and gray[i][j+2]==255:
                gray_last[i][j] = 255
            else:
                gray_last[i][j]=0
    cv.imshow("EdgeDetection_Cur", gray_last)

#加载图片
img = cv.imread("logo.png",1)
#显示彩色图像
cv.imshow("color image",img)
#函数调用
EdgeDetection(img,250, 255)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
