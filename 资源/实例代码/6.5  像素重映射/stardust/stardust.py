#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

#加载图片
img = cv.imread("HelloWorld.png")

mapx = np.zeros(img.shape[:2], dtype=np.float32)
mapy = np.zeros(img.shape[:2], dtype=np.float32)

rows, cons = img.shape[:2]
for i in range(rows):
    for j in range(cons):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv.remap(img, mapy, mapx, cv.INTER_LINEAR)  # mapy表示的是图片高的坐标
cv.imshow('rst', rst)
cv.waitKey()
