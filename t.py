from tkinter import *
from finch import Finch
from time import sleep
from threading import Thread

tweety = Finch()
x, y, z, tap, shake = tweety.acceleration()
global t1


def accel():
    while True:
        global x, y, z, tap, shake
        x, y, z, tap, shake = tweety.acceleration()


def start():
    while True:
        t1.delete(1.0, END)
        s1 = "X is %.2f gees, Y is %.2f gees, Z is %.2f gees" % (x, y, z)
        t1.insert(1.0, s1)


def delete_text():
    t1.delete(1.0, END)


th3 = Thread(target=accel)
th4 = Thread(target=start)

th3.start()
th4.start()

root = Tk()
root.title("Finch with accelerometer")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 200
h = h - 200
root.geometry("400x170".format(w, h))
root.update_idletasks()
b1 = Button(text="Старт", width=15, height=1)
b1.config(command=start)
b1.pack(fill=X, side=BOTTOM)

b2 = Button(text="Стереть", width=15, height=1)
b2.config(command=delete_text)
b2.pack(fill=X, side=BOTTOM)

l1 = Label(text="Нажмите <Старт>",
           font=("Comic Sans MS", 12, "bold"), justify=CENTER)

l1.pack()

t1 = Text(root)

t1.pack(side=BOTTOM)

root.mainloop()
