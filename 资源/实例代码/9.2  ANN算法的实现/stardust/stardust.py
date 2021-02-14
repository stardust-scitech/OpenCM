#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_09
#github    https://github.com/stardust-kevin
#copyright Copyright (C) 2016, Stardust Studio,  All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入数学运算库，定义别名为np
import numpy as np
#导入随机数库
import random

class Network(object):
    """创建构造方法"""
    def __init__(self, sizes):
        self.num_layers = len(sizes) #存储ANN层数
        self.sizes = sizes #存储神经元列表
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]] #生成除第一层外的各神经元偏差，b ≡ −threshold
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])] #生成各神经对应权重ω

    """创建梯度下降函数
    training_data   训练数据
    epochs          训练次数
    mini_batch_size 分批训练过程中每一批训练数据的大小
    eta             学习速率
    """
    def SGD(self, training_data, epochs, mini_batch_size, eta):
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                nabla_b = [np.zeros(b.shape) for b in self.biases]
                nabla_w = [np.zeros(w.shape) for w in self.weights]
                for x, y in mini_batch:
                    delta_nabla_b, delta_nabla_w = self.backprop(x, y)
                    nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
                    nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
                self.weights = [w-(eta/len(mini_batch))*nw
                                for w, nw in zip(self.weights, nabla_w)]
                self.biases = [b-(eta/len(mini_batch))*nb
                               for b, nb in zip(self.biases, nabla_b)]
            print("Epoch {0} complete".format(j))

    """实现反向传播算法"""
    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
        delta = (activations[-1] - y) * self.sigmoid(zs[-1])*(1-self.sigmoid(zs[-1]))
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.sigmoid(z)*(1-self.sigmoid(z))
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    """创建激活函数"""
    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))

#创建4层ANN
Net = Network([8, 4, 4, 1]) 
#输出权重信息
print(Net.weights)
