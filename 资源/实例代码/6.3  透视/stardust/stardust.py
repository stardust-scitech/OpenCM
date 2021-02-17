#file      stardust.py
#author    日有所进, https://blog.csdn.net/fengxueniu/article/details/77964375
#version   
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright 
#license   

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np
 
#角度转弧度函数 
def rad(x):
  return x * np.pi / 180

#加载图片
img = cv.imread("I Love You.png")
#显示原图
cv.imshow("Original image", img)
#扩展图像容器，保证图像不超出可视范围
img = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_CONSTANT, 0)
#获取图像宽度和长度
w, h = img.shape[0:2]
 
#旋转参数
anglex = 0
angley = 0
anglez = 0 
fov = 1

while 1:
  #计算镜头与图像间的距离
  z = np.sqrt(w ** 2 + h ** 2) / 2 / np.tan(rad(fov / 2))

  #创建三维旋转矩阵
  rx = np.array([[1, 0, 0, 0],
          [0, np.cos(rad(anglex)), -np.sin(rad(anglex)), 0],
          [0, -np.sin(rad(anglex)), np.cos(rad(anglex)), 0, ],
          [0, 0, 0, 1]], np.float32)
  ry = np.array([[np.cos(rad(angley)), 0, np.sin(rad(angley)), 0],
          [0, 1, 0, 0],
          [-np.sin(rad(angley)), 0, np.cos(rad(angley)), 0, ],
          [0, 0, 0, 1]], np.float32)
  rz = np.array([[np.cos(rad(anglez)), np.sin(rad(anglez)), 0, 0],
          [-np.sin(rad(anglez)), np.cos(rad(anglez)), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], np.float32)
  r = rx.dot(ry).dot(rz)
 
  #生成四对点
  pcenter = np.array([h / 2, w / 2, 0, 0], np.float32)
  p1 = np.array([0, 0, 0, 0], np.float32) - pcenter
  p2 = np.array([w, 0, 0, 0], np.float32) - pcenter
  p3 = np.array([0, h, 0, 0], np.float32) - pcenter
  p4 = np.array([w, h, 0, 0], np.float32) - pcenter
  dst1 = r.dot(p1)
  dst2 = r.dot(p2)
  dst3 = r.dot(p3)
  dst4 = r.dot(p4)
  list_dst = [dst1, dst2, dst3, dst4]
  org = np.array([[0, 0],
          [w, 0],
          [0, h],
          [w, h]], np.float32)
  dst = np.zeros((4, 2), np.float32)
 
  #投影至成像平面
  for i in range(4):
    dst[i, 0] = list_dst[i][0] * z / (z - list_dst[i][2]) + pcenter[0]
    dst[i, 1] = list_dst[i][1] * z / (z - list_dst[i][2]) + pcenter[1]
 
  #通过四对点计算透射变换
  warpR = cv.getPerspectiveTransform(org, dst)
  #对图像进行透视变换
  result = cv.warpPerspective(img, warpR, (h, w))
  #显示变换后的图片
  cv.imshow("Result", result)
  #获取键盘键值
  c = cv.waitKey(0)
 
  #anglex += 0.1    
  #anglez += 0.1       
  #angley += 0.1      
 
  #键盘控制
  if 27 == c:
    break;
  if c == ord('w'):
    anglex += 1
  if c == ord('s'):
    anglex -= 1
  if c == ord('a'):
    angley += 1
  if c == ord('d'):
    angley -= 1
  if c == ord('u'):
    anglez += 1
  if c == ord('p'):
    anglez -= 1
  if c == ord('t'):
    fov += 1
  if c == ord('r'):
    fov -= 1
  if c == ord(' '):
    anglex = angley = anglez = 0
  if c == ord('q'):
    print("======================================")
    print("旋转矩阵：\n", r)
    print("angle alpha: ", anglex, 'angle beta: ', angley, "dz: ", anglez, ": ", z)
