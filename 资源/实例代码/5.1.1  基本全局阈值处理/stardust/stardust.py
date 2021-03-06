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

def threshold_binary(img): 
	#BGR(OpenCV使用BGR而非RGB格式)转灰度图像 
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
	#图像转为一维数组并获得灰度直方图以便调整算法的使用 
	plot.hist(img.ravel(), 256, [0, 256]) 
	#显示直方图窗口 
	plot.show() 
	#局部特征峰值为160 
	ret, binary = cv.threshold(gray, 160, 255, cv.THRESH_BINARY) 
	#窗口输出指定图像 
	cv.imshow("Threshold binary", binary) 
	#输出窗口打印参数 
	print("二值化阈值: %s" % ret) 

#加载图片 
img = cv.imread("landscape.jpg") 
#显示彩色图像 
cv.imshow("Color image",img) 
#函数调用 
threshold_binary(img) 
#等待按下任意按键继续运行下一条语句 
cv.waitKey(0) 
