#tracks mouse position (and shows it)

import pyautogui
from tkinter import *
import time

#fix resolution for windows 10
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

#create window
tk = Tk()
tk.title('Mouse Pointer Information')

#fill widgets into the window created above
canvas = Canvas(tk, width=450, height=200)
canvas.pack()
ct = canvas.create_text(200, 50, text='0000000', fill='red',font=('Courier', 15))
ct2 = canvas.create_text(200, 100, text='0000000', fill='red',font=('Courier', 15))
ct3col = canvas.create_rectangle(230,130,250,150, fill='red')
ct4time = canvas.create_text(350, 180, text='0000000', fill='grey',font=('Courier', 10))

#loop
while 1==1:
    pos = pyautogui.position()
    pixcol = pyautogui.screenshot().getpixel(pos)
    
    canvas.itemconfig(ct, text="position: " + str(pos))
    canvas.itemconfig(ct2, text="color: " + str(pixcol))
    ccc='#%02x%02x%02x' % (pixcol[0], pixcol[1], pixcol[2])
    canvas.itemconfig(ct3col, fill=ccc)
    canvas.itemconfig(ct4time, text=str(time.asctime()))
    
    tk.update()
