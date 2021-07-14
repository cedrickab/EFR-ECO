import classify
import base64
import tkinter
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk
import numpy as np
from PIL import Image

imagePath = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('jpg files','.jpg'),('bmp files','.bmp'),('all files','.*')])
result = classify.analyse(imagePath)

a = "we think this is a {0} with a certainty of {1} %".format(result[0], float(result[1]) * 100)



tkinter.messagebox.showinfo("EFRE'CO", a)
