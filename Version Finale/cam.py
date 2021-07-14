# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:07:13 2021

@author: hp
"""

"""
import cv2
def show_webcam(mirror=False, width=600, height=600):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        cv2.namedWindow('my webcam',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('my webcam', width, height)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()
"""

import cv2

import classify

import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk
import numpy as np
from PIL import Image

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        import classify
        resultcam =classify.analyse(img_name)
        import GPS

        a = "we think this is a {0} with a certainty of {1} %".format(resultcam[0], float(resultcam[1]) * 100)

        tkinter.messagebox.showinfo("EFRE'CO", a)


cam.release()

cv2.destroyAllWindows()
