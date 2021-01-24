from tkinter import *
from finch import Finch
from time import sleep


def start():

    t1.delete(1.0, END)
    tweety = Finch()

    left, right = tweety.obstacle()
    x, y, z, tap, shake = tweety.acceleration()
    x1 = str(x)
    y1 = str(y)
    z1 = str(z)
    s1 = "x is ", x1, " y is ", y1, " z is ", z1
    t1.insert(1.0, s1)

def delete_text():
    t1.delete(1.0, END)










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

b2 = Button(text = "Стереть", width=15, height=1)
b2.config(command=delete_text)
b2.pack(fill=X, side=BOTTOM)

l1 = Label(text="Нажмите <Старт>",
           font=("Comic Sans MS", 12, "bold"), justify=CENTER)

l1.pack()


t1 = Text(root)




t1.pack(side = BOTTOM)


root.mainloop()
