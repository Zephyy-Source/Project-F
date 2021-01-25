from tkinter import *

def start():
    b1['text'] = "Робот подключен"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
    l1['text'] = "Отображение робота"
    l1['font'] = "Comic Sans MS", 12, "italic"
    l1['width'] = 50
    l1['height'] = 25
    l1['bg'] = '#9ad9ab'

root = Tk()
root.title("Finch with gyroscope")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 200
h = h - 200
root.geometry('+{}+{}'.format(w,h))

b1 = Button(text= "Подключить робота", width = 15, height = 3)
b1.config(command = start)
b1.pack(fill = X, side=BOTTOM)

l1 = Label(text = "Здесь будет отображаться моделька робота в таком же положении как и он сам в пространстве",
           font = ("Comic Sans MS", 12, "bold"), justify = CENTER)
l1.pack()




root.mainloop()