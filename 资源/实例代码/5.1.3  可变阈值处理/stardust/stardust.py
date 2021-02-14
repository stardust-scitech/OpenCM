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

def threshold_average(img,a):  
    #BGR(OpenCV使用BGR而非RGB格式)转灰度图像  
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
    gray_last = gray  
    #历遍每个像素元素并处理  
    for i in range(len(gray)):  
        for j in range(len(gray[0])):  
            if i>10 and i<310 and j>10 and j<310:  
                average = (gray_last[i-1][j-1]+gray_last[i-1][j]+gray_last[i-1][j+1]+  
                            gray_last[i][j-1]   +gray_last[i][j]   +gray_last[i][j+1]+  
                            gray_last[i+1][j-1]+gray_last[i+1][j]+gray_last[i+1][j+1])/9  
                if gray[i][j] > average*a:  
                    gray[i][j] = 255  
                else:  
                    gray[i][j] = 0  
            else:  
                gray[i][j] = 0  
    #窗口输出指定图像  
    cv.imshow("Threshold multi", gray)  
  
#加载图片  
img = cv.imread("landscape.jpg",1)  
#显示彩色图像  
cv.imshow("color image",img)  
#函数调用  
threshold_average(img,7)  
#等待按下任意按键继续运行下一条语句  
cv.waitKey(0)  
#释放HighGUI窗口  
#cv.destroyAllWindows()  
