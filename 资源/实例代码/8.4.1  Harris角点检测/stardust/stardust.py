#file stardust.py
#author 凡尘(Kevin Brooks)
#version 1.0
#date 2020_08_04
#github https://github.com/stardust-kevin
#copyright Copyright (C) 2016, Stardust Studio,  All Rights Reserved
#license http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#载入图片
img = cv.imread("box.png")
#BGR转灰度
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#整数转浮点
gray = np.float32(gray)
#角点检测
dst = cv.cornerHarris(gray,5,3,0.05)
#标记点膨胀
dst = cv.dilate(dst,None)
#角点筛选
img[dst>0.01*dst.max()]=[0,0,255]
#显示处理图像
cv.imshow("Harris image", img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
