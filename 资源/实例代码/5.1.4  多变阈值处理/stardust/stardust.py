#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入2D绘图库功能模块，定义别名为plot
from matplotlib import pyplot as plot 

def threshold_rgb(img, t1, t2, t3): 
    #BGR(OpenCV使用BGR而非RGB格式)转灰度图像   
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    #历遍每个像素元素并处理 
    for i in range(len(img)): 
        for j in range(len(img[0])): 
            for k in range(len(img[0][0])): 
                if img[i][j][k]>t1 and img[i][j][k]>t2 and img[i][j][k]>t3: 
                    gray[i][j] = 255 
                else: 
                    gray[i][j] = 0 
    #窗口输出指定图像 
    cv.imshow("Threshold change", gray) 
 
#加载图片 
img = cv.imread("landscape.jpg",1) 
#创建窗口 
cv.namedWindow("FixedThreshold",cv.WINDOW_NORMAL) 
#显示彩色图像 
cv.imshow("color image",img) 
#函数调用 
threshold_rgb(img, 70, 90, 80) 
#等待按下任意按键继续运行下一条语句 
cv.waitKey(0) 
