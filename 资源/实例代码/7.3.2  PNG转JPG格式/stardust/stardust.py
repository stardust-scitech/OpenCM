#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

import os
import cv2
import sys
import numpy as np

filename = "lab"  

img = cv2.imread("lab.png")
print(filename.replace(".png",".jpg"))
newfilename = filename.replace(".png",".jpg")
cv2.imwrite("new.jpg",img)
