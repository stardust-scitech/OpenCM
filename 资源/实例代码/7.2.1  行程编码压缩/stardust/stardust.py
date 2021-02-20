#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入基本功能cv2库
import cv2 as cv
#导入数学运算库对象
import numpy as np

#加载图片
img = cv.imread("HelloWorld.png")
#显示压缩前图像
cv.imshow("rec_image_pre",img)
#BGR转灰度
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#获取图像宽度和长度像素值
rows, cols = gray.shape
#图像转一维列表
image1 = gray.flatten()
#图像二值化
ret, image1 = cv.threshold(image1, 127, 255, cv.THRESH_BINARY)

#初始化中间变量
data = []
image3 = []
count = 1

#行程压缩编码
for i in range(len(image1)-1):
    if (count == 1):
        image3.append(image1[i])
    if image1[i] == image1[i+1]:
        count = count + 1
        if i == len(image1) - 2:
            image3.append(image1[i])
            data.append(count)
    else:
        data.append(count)
        count = 1
if(image1[len(image1)-1] != image1[-1]):
    image3.append(image1[len(image1)-1])
    data.append(1)

#计算压缩率
ys_rate = len(image3)/len(image1)*100
#显示压缩率
print("压缩率为" + str(ys_rate) + '%')

#行程编码解码
rec_image = []
for i in range(len(data)):
    for j in range(data[i]):
        rec_image.append(image3[i])

#重构图像
rec_image = np.reshape(rec_image,(rows,cols))
#保存压缩后的图像
cv.imwrite("HelloWorld2.png", rec_image)
#显示压缩后的图像
cv.imshow("rec_image",rec_image)
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
