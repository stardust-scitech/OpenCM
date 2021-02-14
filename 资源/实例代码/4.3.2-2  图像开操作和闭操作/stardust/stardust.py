#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_03
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv

#创建结构单元
kernel=cv.getStructuringElement(cv.MORPH_RECT,(9,9))
#加载图片
img=cv.imread("HelloWorld.png")
#开运算
img_close=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
#显示彩色图像
cv.imshow("Color image",img)
#显示处理后图像
cv.imshow("Close image",img_close)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
