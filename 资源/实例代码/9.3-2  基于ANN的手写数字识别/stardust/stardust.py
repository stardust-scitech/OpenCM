#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_10
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2016, Stardust Studio,  All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入神经网络库，定义别名为network
import Libraries.Network.network as network
#导入MNIST加载库，定义别名为mnist_loader
import Libraries.Network.mnist_loader as mnist_loader

#加载MNIST数据库
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
#初始化神经网络
net = network.Network([784, 30, 10])
#调用梯度下降算法开始训练神经网络
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
