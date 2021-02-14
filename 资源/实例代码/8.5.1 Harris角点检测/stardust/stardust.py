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


filename = 'board.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.1)
dst = cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()