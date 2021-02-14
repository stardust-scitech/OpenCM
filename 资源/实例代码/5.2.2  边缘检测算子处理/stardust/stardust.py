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

def EdgeDetection(img):
    #BGR(OpenCV使用BGR而非RGB格式)转灰度图像  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    #图像转为一维数组并获得灰度直方图以便调整算法的使用
    plot.hist(gray.ravel(), 256, [0, 256])
    #显示直方图窗口
    plot.show()
    #高斯滤波降噪
    gauss = cv.GaussianBlur(gray, (3, 3), 0)  
    #20对应最小阈值,160对应最大阈值
    canny = cv.Canny(gray, 0, 10) 
    #显示边缘处理后图像
    cv.imshow("EdgeDetection", canny)

#加载图片
img = cv.imread("logo.png",1)
#显示彩色图像
cv.imshow("color image",img)
#函数调用
EdgeDetection(img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
