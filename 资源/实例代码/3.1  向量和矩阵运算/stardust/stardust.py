#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_09_10
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入数学运算库，定义别名为np
import numpy as np

#构造2x2矩阵
a=np.array([[1.1, 2.2],[3.3, 4.4]])
#矩阵点乘
b=a*a 
#矩阵点乘
c=np.multiply(a,a)
#矩阵叉乘
d=np.dot(a, a)
#输出运算结果
print("[矩阵点乘]a*a=\n",b) 
print("[矩阵点乘]multiply(a,a)=\n",c)
print("[矩阵叉乘]dot(a,a)=\n",d)
