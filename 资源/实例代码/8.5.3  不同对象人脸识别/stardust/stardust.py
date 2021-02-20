#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2021_02_19
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入cv2模块，定义别名为cv
import cv2 as cv
#导入采样模块，定义别名为st
import sample_take as st
#导入识别模块，定义别名为sc
import sample_check as sc

#定义文件夹路径
file_path = "./sample/"
#定义待识别的对象名称
check = ["stardust"]
#人脸采样次数
check_times = 100
#开启电脑摄像头
cap = cv.VideoCapture(0)
#键盘控制
print("--------------------Program start--------------------")
print("[Main menu]Please select operation mode or quit")
while 1:
    ret, frame = cap.read()
    cv.imshow("Captured image", frame)
    key_mode = cv.waitKey(1)
    #退出程序
    if key_mode == 27:
        print("--------------------Quit program--------------------")
        break;
    #进行人脸采集
    elif key_mode == ord('a'):
        while 1:
            ret, frame = cap.read()
            cv.imshow("Image", frame)
            key_mode = cv.waitKey(1)
            if key_mode == 27:
                break;
    elif key_mode == ord('t'):
        print("--------------------Start take--------------------")
        print("[Second menu]Please select person to take picture or quit")
        while 1:
            ret, frame = cap.read()
            cv.imshow("Captured image", frame)
            key_mode = cv.waitKey(1)
            if key_mode == 27:
                cap = cv.VideoCapture(0)
                print("--------------------Stop take--------------------")
                print("[Main menu]Please select operation mode or quit")
                break;
            elif key_mode>=48 and key_mode<=57:
                cap = cv.VideoCapture(0)
                print("--------------------Start take--------------------")
                st.take_sample(file_path, check[key_mode-48], check_times)
                print("--------------------Take successed--------------------")
                print("[Second menu]Please select person to take picture or quit")
            elif key_mode>-1:
                print("Error key mode")
    #进行人脸识别
    elif key_mode == ord('c'):
        check_flag = 0
        if check_flag==0:
            print("--------------------Start check--------------------")
            print("[Second menu]You can press 'ESC' to stop check")
            check_flag = 1
        sc.check_sample(file_path)
        cap = cv.VideoCapture(0)
        print("--------------------Stop check--------------------")
        print("[Main menu]Please select operation mode or quit")
        check_flag = 0
    elif key_mode>-1:
        print("Error key mode")
