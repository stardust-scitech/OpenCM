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

#打开文件并以字节形式读取内容
file = open("./MNIST/t10k-images.idx3-ubyte",'rb').read()
#截取读取的内容，共计784字节，偏移16字节
img = np.frombuffer(file,dtype=np.uint8,count=784,offset=16)
#重构信息为28x28二维列表
img=img.reshape(28,28) 
"""
将图像数据归一化
img=img.reshape(28,28)/256.0 
"""
#输出列表信息
print(img)
#重构图片，比例放大20倍
img = cv.resize(img, None, fx=20, fy=20, interpolation=cv.INTER_AREA)
#显示处理图像
cv.imshow("Resized image", img)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
