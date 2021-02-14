#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_07
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

import fnmatch
import os
import pandas as pd
import numpy as np  
import sys
import cv2

def ReadSaveAddr(Stra,Strb):
    #print(Stra)
    #print(Strb)
    print("Read :",Stra,Strb)
    a_list = fnmatch.filter(os.listdir(Stra),Strb)
    print("Find = ",len(a_list))
    df = pd.DataFrame(np.arange(len(a_list)).reshape((len(a_list),1)),columns=['Addr'])  
    df.Addr = a_list

    for i in range(len(a_list)):
        path = Stra+'/'+a_list[i]
        #print(path)
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        #print(img.shape)
        temp = np.ones((88,60))
        for m in range(88):
            for n in range(60):
                temp[m,n] = img[m,n]
        #print(temp.shape)
        t = a_list[i]
        t = t[:-4]
        t = 'D:/test/New/'+t+'.bmp'
        #cv2.imwrite(t,img)
        cv2.imwrite(t,temp)

    df.to_csv('Get.lst',columns=['Addr'],index=False,header=False)
    print("Write To Get.lst !")

ReadSaveAddr("lab.png","new.bmp")
