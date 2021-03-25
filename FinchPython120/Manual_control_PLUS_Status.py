from tkinter import *
import keyboard
import time
import thread

def print_tim
    e(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))

 try:
    thread.start_new_thread( print_time, ("Thread-1", 2,))
    thread.start_new_thread( print_time, ("Thread-2", 4,))
 except:
    print("Error")

#####################################################

def close():
    window.destroy();


def clicked():
    exec(open("Manual_control.py").read());

window = Tk()
window.title("ULtraMegaGui v.0.1")
window.geometry('720x360')
lbl = Label(window, text="Hello", font=("Arial", 40))
lbl.grid(column=0, row=0)
btn = Button(window, text="ТЕСТ", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
