#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_15
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np
#导入随机数库
import random
#导入数学库
import math

#生成画布
img = np.zeros((480, 640, 3), np.uint8) 

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画点，坐标为(10, 240)对应x轴和反y轴
img[240, 10] = color

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画线，起点为(0, 0)，终点为(200, 200)，线径为2
cv.line(img, (0, 0), (200, 200), color, 2)

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画圆，圆心为，(320, 240)，半径为10，随机颜色，实心填充
cv.circle(img, (320, 240), 20, color, -1)

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画椭圆，中心点(200, 200)，短半轴100，长半轴70，逆时针10度，角度范围(0, 200)，随机颜色，线径为2
cv.ellipse(img, (255, 255), (100, 70), 10, 0, 200, color, 2)

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画三角形和多边形，三个坐标点为(500, 190)、(220, 420)、(120, 50)，封闭绘图，随机颜色，线径为2
cv.polylines(img, [np.array([[500, 190], [220, 420], [120, 50]])], True, color, 2)

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画矩形，左上角点(30, 30),右下角点(180 ,200)，随机颜色，线径为2
cv.rectangle(img, (30, 30), (180 ,200), color, 2)

#定义绘制的三角形中心点坐标
CenterCoordinate = np.array([100, 350])
#定义边长
SideLength = 100
#定义旋转角度
RotateAngle = 90
#构建三角形顶点坐标
VertexCoordinates = np.array([[CenterCoordinate[0], int(CenterCoordinate[1]-SideLength*math.sqrt(3)/3)], 
                  [int(CenterCoordinate[0]-SideLength/2), int(CenterCoordinate[1]+SideLength*math.sqrt(3)/6)], 
                  [int(CenterCoordinate[0]+SideLength/2), int(CenterCoordinate[1]+SideLength*math.sqrt(3)/6)]])
#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#连接三角形顶点
cv.polylines(img, [VertexCoordinates], True, color, 2)
#输出变换前三角形顶点坐标
print(VertexCoordinates)

#旋转变换函数
def Rotation(array, center, angle):
    #历遍每个像素元素并处理
    angle = math.pi*angle/180
    AngleCur = np.array([[array[0][0], array[0][1]], [array[1][0], array[1][1]], [array[2][0], array[2][1]]])
    for i in range(len(array)):
        array[i][0] = int((AngleCur[i][0]-center[0]) * math.cos(angle) - (AngleCur[i][1]-center[1]) * math.sin(angle) + center[0]);
        array[i][1] = int((AngleCur[i][0]-center[0]) * math.sin(angle) + (AngleCur[i][1]-center[1]) * math.cos(angle) + center[1]);
#调用旋转变换函数
Rotation(VertexCoordinates, CenterCoordinate, RotateAngle)

#指定绘图颜色
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
#画变换三角形，三个坐标点为(500, 190)、(220, 420)、(120, 50)，封闭绘图，随机颜色，线径为2
cv.polylines(img, [VertexCoordinates], True, color, 2)
#输出变换后三角形顶点坐标
print(VertexCoordinates)

#显示彩色图像
cv.imshow('image', img)

#等待按下任意按键继续运行下一条语句
cv.waitKey(0)