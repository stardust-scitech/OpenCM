#file stardust.py
#author 凡尘(Kevin Brooks)
#version 1.0
#date 2020_08_04
#github https://github.com/stardust-kevin
#copyright Copyright (C) 2016, Stardust Studio,  All Rights Reserved
#license http://www.apache.org/licenses/LICENSE-2.0

#导入基本功能cv2库
import cv2
import numpy as np

# 读取名称为 p20.png 的图片，并转成黑白
img = cv2.imread("scenery.jpg",1)
gray = cv2.imread("scenery.jpg",0)

cv2.imshow("img_template",cv2.imread("boy.jpg"))
# 读取需要检测的模板图片（黑白）
img_template = cv2.imread("boy.jpg",0)
# 得到图片的高和宽
w, h = img_template.shape[::-1]
print(w,h)

# 模板匹配操作
res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF)

# 得到最大和最小值得位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc #左上角的位置
bottom_right = (top_left[0] + w, top_left[1] + h) #右下角的位

# 在原图上画矩形
cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)

# 显示处理后的图像
cv2.imshow("processed",img)
cv2.waitKey(0)
