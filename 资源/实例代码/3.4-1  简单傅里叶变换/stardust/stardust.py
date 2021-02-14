#file      stardust.py
#author    http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/tutorials.html
#version   
#date      2020_09_11
#github    https://github.com/stardust-scitech/OpenCM
#copyright 
#license   

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np
#导入绘图模块，定义别名为plt
import matplotlib.pyplot as plt

#导入图像并转化为灰度图像
img = cv.imread('fish.jpg', 0)
#将空间域转换为频率域
f = np.fft.fft2(img)
#使零频率分量居中
fshift = np.fft.fftshift(f)
#转化负数、取对数并20倍扩大指数
magnitude_spectrum = 20 * np.log(np.abs(fshift))
#pyplot绘图
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()