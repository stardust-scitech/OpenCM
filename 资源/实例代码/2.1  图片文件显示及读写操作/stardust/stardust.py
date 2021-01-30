#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_07
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库
import numpy

#加载图片
img = cv.imread("HelloWorld.png", cv.IMREAD_UNCHANGED)
#调用输出窗口
print(len(img))
#索引修改图像
img[:, :, 0] = 0
#调用输出窗口
print(img)
#显示彩色图像
cv.imshow("HelloWorld image",img)

#构造图像
img2 = numpy.zeros((3,3), dtype=numpy.uint8)
#修改单一点像素值
img2[1,1] = 255
#显示构造图像
cv.imshow("Structure image",img2)

#复制图像
img3 = img
#区域化赋值
img[100:200, 100:200]=0
#分割图像
imgPre = img3[100:200, 100:200]
#组合图像
img3[200:300, 80:180] = imgPre
#显示组合图像
cv.imshow("Combination image",img3)

#调用输出窗口
print("HelloWorld")
#等待保存按键按下
if cv.waitKey(0) == ord('s'): 
    cv.imwrite('HelloWorld_2.png',img3)
