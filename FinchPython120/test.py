from tkinter import *
from finch import Finch
from time import sleep
from threading import Thread

fin = Finch()
x, y, z, tap, shake = fin.acceleration()

def accel():
    global x, y, z, tap, shake
    while True:
        x, y, z, tap, shake = fin.acceleration()

def looping():
    while  True:
        t1.delete(1.0, END)
        s1 = "X is %.2f , Y is %.2f , Z is %.2f " % (round(x, 2), round(y, 2), round(z, 2))
        t1.insert(1.0, s1)
        sleep(0.5)

def start():
    th4.start()


def delete_text():
    t1.delete(1.0, END)


th4 = Thread(target=looping)
th3 = Thread(target=accel)
th3.start()

root = Tk()
root.title("Finch with accelerometer")
root.geometry("400x170")
root.update_idletasks()

b1 = Button(text="Старт", width=15, height=1, command=start)
b1.pack(fill=X, side=BOTTOM)

b2 = Button(text="Стереть", width=15, height=1, command=delete_text)
b2.pack(fill=X, side=BOTTOM)

l1 = Label(text="Нажмите <Старт>", font=("Comic Sans MS", 12, "bold"), justify=CENTER)
l1.pack()
t1 = Text(root)
t1.pack(side=BOTTOM)

root.mainloop()
