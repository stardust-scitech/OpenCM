#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_13
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入time模块
import time

#延时时间，单位ms
G_DelayTimes = 1

#读取摄像头视频流
video = cv.VideoCapture(0)
#定义编解码器
save = cv.VideoWriter('save.avi', cv.VideoWriter_fourcc(*'XVID'), 30, (640, 480), 0)

#截止时间戳
end = 0
#开始时间戳
start = 0
#有效帧计数器
count0 = 0
#总帧数计数器
count1 = 0

while video.isOpened():
    #计算时间差
    end = time.time()
    times = end-start
    start = time.time()
    #估算帧率
    fps  = 1 / times
    #总帧数记数
    count1+=1
    #有效帧计数
    if fps>29 and fps<31:
        count0+=1
    #逐帧读取
    ret, frame = video.read()
    #帧读取成功，ret的值为True
    if not ret:
        print("帧读取失败")
        break
    #输出窗口输出帧率
    print(fps)
    #灰度处理
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #帧写入
    save.write(gray)
    #显示灰度图像
    cv.imshow("Gray video", gray)
    #等待退出按键按下
    if cv.waitKey(G_DelayTimes) == ord('r'):
        break

#释放帧捕获器
#video.release()
#释放帧保存器
#save.release()