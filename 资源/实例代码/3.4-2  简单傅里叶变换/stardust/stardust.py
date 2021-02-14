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
img = cv.imread('fish.jpg',0) #直接读为灰度图像
#创建掩码，中心正方形为0，其余全为1
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
mask1 = np.ones(img.shape,np.uint8)
mask1[crow-20:crow+20,ccol-20:ccol+20] = 0
mask2 = np.zeros(img.shape,np.uint8)
mask2[crow-80:crow+80,ccol-80:ccol+80] = 1
mask = mask1*mask2
# 应用掩码和逆DFT
f1 = np.fft.fft2(img)
f1shift = np.fft.fftshift(f1)
#掩码矩阵和原图矩阵点乘
f1shift = f1shift*mask
f2shift = np.fft.ifftshift(f1shift)
img_new = np.fft.ifft2(f2shift)
img_new = np.abs(img_new)
#pyplot绘图
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_new, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()