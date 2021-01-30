#导入基本功能cv2库
import cv2 as cv

#延时时间，单位ms
G_DelayTimes = 40

#读取缓存视频
video = cv.VideoCapture("wave.mp4")
#循环处理
while video.isOpened():
    #逐帧读取
    ret, frame = video.read()
    #帧读取成功，ret的值为True
    if not ret:
        print("帧读取失败")
        break
    #灰度处理
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #显示灰度图像
    cv.imshow('frame', gray)
    #等待退出按键按下
    if cv.waitKey(G_DelayTimes) == ord('r'):
        break
#释放帧捕获器
video.release()