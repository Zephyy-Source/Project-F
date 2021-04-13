from tkinter import *
import keyboard
import time
import sys
from threading import Thread


def close():
    window.destroy()


def eliminate():
    sys.exit()

def clicked():
    close()
    th1 = Thread(target=anotherWindow())
    th1.start()
    th2 = Thread(target=(exec(open("Manual_control.py").read())))
    th2.start()

def anotherWindow():
    window2 = Tk()
    window2.title("ULtraMegaGui v.0.1")
    window2.geometry('720x360')
    lbl = Label(window2, text="Hello", font=("Arial", 40))
    lbl.grid(column=0, row=0)
    btn = Button(window2, text="ТЕСТ", command=clicked)
    btn.grid(column=1, row=0)
    btn1 = Button(window2, text='Close programm', command=eliminate)
    btn1.grid(column =2, row =1)
    window2.mainloop()


window = Tk()
window.title("ULtraMegaGui v.0.1")
window.geometry('720x360')
lbl = Label(window, text="Hello", font=("Arial", 40))
lbl.grid(column=0, row=0)
btn = Button(window, text="ТЕСТ", command=clicked)
btn.grid(column=1, row=0)
btn1 = Button(window, text='Close programm', command=eliminate)
btn1.grid(column =2, row =1)
window.mainloop()
