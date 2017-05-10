#tracks mouse position (and shows it) for a short(?) time...

import pyautogui
from tkinter import *
import time

from ctypes import windll         #fix resolution for windows 10
user32 = windll.user32
user32.SetProcessDPIAware()

tk = Tk()   #<var> = Tk()    #create the window to do stuff in
tk.title('sfsdfgh')

canvas = Canvas(tk, width=450, height=200)
canvas.pack()
ct = canvas.create_text(200, 50, text='0000000', fill='red',font=('Courier', 15))
ct2 = canvas.create_text(200, 100, text='0000000', fill='red',font=('Courier', 15))
ct3col = canvas.create_rectangle(230,130,250,150, fill='red')
ct4time = canvas.create_text(350, 180, text='0000000', fill='grey',font=('Courier', 10))

i=0
while 1==1:
    pos = pyautogui.position()
    pixcol = pyautogui.screenshot().getpixel(pos)
    
    canvas.itemconfig(ct, text="position: " + str(pos))
    canvas.itemconfig(ct2, text="color: " + str(pixcol))
    ccc='#%02x%02x%02x' % (pixcol[0], pixcol[1], pixcol[2])
    canvas.itemconfig(ct3col, fill=ccc)
    canvas.itemconfig(ct4time, text=str(time.asctime()))
    
    i=i+1
    if i == 9999999999999999:
        pyautogui.alert("time's up. sayounara...")
        break
    tk.update()
