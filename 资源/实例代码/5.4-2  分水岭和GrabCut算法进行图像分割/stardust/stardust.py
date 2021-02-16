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
#导入绘图模块，定义别名为plt
from matplotlib import pyplot as plt

#加载图片
img = cv.imread("apple.jpg")
#创建掩膜
mask = np.zeros(img.shape[:2],np.uint8)
#构建背景模型
bgdModel = np.zeros((1,65),np.float64)
#构建前景模型
fgdModel = np.zeros((1,65),np.float64)
#定义矩形框
rect = (0,0,479,639)
#grabCut算法处理
cv.grabCut(img,mask,rect,bgdModel,fgdModel,2,cv.GC_INIT_WITH_RECT)
#创建掩膜用来过滤
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#重新计算着色
img = img*mask2[:,:,np.newaxis]
#pyplot绘图
plt.imshow(img),plt.colorbar(), plt.show()
