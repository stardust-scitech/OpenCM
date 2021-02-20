#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   蓝一潇、薛定谔的猫, https://blog.csdn.net/weixin_42744102/article/details/105537892
#date      2020_08_07
#github    https://github.com/stardust-scitech/OpenCM
#copyright 
#license   

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入数学运算库，定义别名为np
import numpy as np

class ArtimeticCoding(object):
    def __init__(self, symbol, P, _range=1., _low=0.):
        self.__symbol = [str(s) for s in symbol]
        self.__P = P
        self.__range = _range
        self.__low = _low
        if sum(self.__P) > 1.:
            raise Exception('InitialError', 'Probability sum bigger than 1.')
        if len(self.__P) != len(self.__symbol):
            raise Exception('InitialError', 'Probability and symbol not match.')
        self.__map = self.__symbol_map()

    def __symbol_map(self):
        __map = {}
        __mark = 0.
        for sidx in range(len(self.__symbol)):
            __map[self.__symbol[sidx]] = {'from': __mark, 'to': __mark + self.__P[sidx]}
            __mark += self.__P[sidx]
        return __map

    def encode(self, seq=''):
        return self.__encode(seq, self.__range, self.__low)

    def __encode(self, s, __range, __low):
        if s[0] not in self.__map:
            raise Exception('SymbolError', 'unknown symbol occurred.')
        __low2 = __low + __range * self.__map[s[0]]['from']
        __high2 = __low + __range * self.__map[s[0]]['to']
        # print(s[0], __high2, __low2)
        if len(s) == 1:
            return __low2
        else:
            return self.__encode(s[1:], __high2 - __low2, __low2)

#加载图片
img = cv.imread("lab.jpg")
#将图像转为一维矩阵
flatten = img.flatten()
#求取数据总和，加一防止数据溢出
flatten_sum = sum(flatten.tolist())+1
#数据归一化
flatten = flatten/flatten_sum
#进行算术编码
data = ArtimeticCoding(list(range(len(flatten))), flatten)
#输出编码结果
print(data.encode('10101'))
