#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_04
#github    https://github.com/stardust-kevin
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

#导入基本功能cv2库
import cv2 as cv

#加载图片
img = cv.imread("HelloWorld.png")
#显示彩色图像
cv.imshow("HelloWorld image",img)
#调用输出窗口
print("HelloWorld")
#等待按下任意按键继续运行下一条语句
cv.waitKey(0)
#释放HighGUI窗口
#cv.destroyAllWindows()
