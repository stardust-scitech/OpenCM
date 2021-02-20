#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_18
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#加载目标图片
img_target = cv.imread("scenery.jpg")
#BGR转灰度
gray_target = cv.cvtColor(img_target, cv.COLOR_BGR2GRAY)
#加载模板图片
img_template = cv.imread("boy.jpg")
#BGR转灰度
gray_template = cv.cvtColor(img_template, cv.COLOR_BGR2GRAY)
#获取图像宽度和长度
rows, cons = img_template.shape[:2]
#进行模板匹配操作
val = cv.matchTemplate(gray_target,gray_template,cv.TM_SQDIFF)
#获取矩阵的最小值和最大值，并得到对应值索引
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(val)
#模板图片在目标图片的坐上角坐标
top_left = min_loc
#模板图片在目标图片的右下上角坐标
bottom_right = (min_loc[0] + rows, min_loc[1] + cons) #右下角的位
#在目标图片上框选模板图片
cv.rectangle(img_target,top_left, bottom_right, (0,0,255), 4)
#显示模板图片
cv.imshow("Template image", img_template)
#显示匹配后的图片
cv.imshow("Matched image",img_target)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
