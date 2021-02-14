#file      stardust.py
#author    Joseph Howse, Learning OpenCV 3 Computer Vision with Python - Second Edition
#version   
#date      2020_09_11
#github    https://github.com/stardust-scitech/OpenCM
#copyright 
#license   

#导入基本功能cv2库
import cv2
#导入managers管理类
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.enterFrame
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    def onKeypress(self,keycode):
        if keycode == 32:  #space
            self._captureManager.writeImage('Cameo.png')
        elif keycode == 9:  #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('Cameo.mp4')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: #escape
            self._windowManager.destoryWindow()
if __name__ == "__main__":
    Cameo().run()