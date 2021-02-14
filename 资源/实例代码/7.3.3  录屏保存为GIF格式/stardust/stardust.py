#file      stardust.py
#author    凡尘(Kevin Brooks)
#version   1.0
#date      2020_08_07
#github    https://github.com/stardust-scitech/OpenCM
#copyright Copyright (C) 2018, Stardust Studio, All Rights Reserved
#license   http://www.apache.org/licenses/LICENSE-2.0

import os
import cv2
import sys
import numpy as np

import cv2
import imageio

def read_video(video_path):
    video_cap = cv2.VideoCapture(video_path)
    frame_count = 0
    all_frames = []
    while True:
        ret, frame = video_cap.read()
        if ret is False:
            break
        all_frames.append(frame)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        frame_count += 1
        print(frame_count)
    video_cap.release()
    cv2.destroyAllWindows()
    print('===>', len(all_frames))

    return all_frames


def frame_to_gif(frame_list):
    gif = imageio.mimsave('./result.gif', frame_list, 'GIF')


if __name__ == "__main__":
    frame_list = read_video('demo.mp4')
    frame_to_gif(frame_list)