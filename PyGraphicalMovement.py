import tkinter as tk
from tkinter import ttk


def Draw_button(window):
    x, y = 10, 0
    arr = []
    for i in range(3):
        arr.append([])
        for j in range(3):
            arr[i].append(tk.Button(height="5", width="5"))
            arr[i][j].grid(column=x, row=y)
            x += 10
        x = 10
        y += 8
    return arr


def Draw_tabs(window):
    tabs = tk.ttk.Notebook(window)
    tab1 = tk.ttk.Frame(tabs)
    tab2 = tk.ttk.Frame(tabs)
    tabs.add(tab1, text='Matrix')
    tabs.add(tab2, text='Arrows')
    tabs.pack(expand=1, fill='both')
    return tabs


win = tk.Tk()
win.title("PyFinchMovement")
win.geometry("205x300")
#  buttons = Draw_button(win)
tabs = Draw_tabs(win)
win.mainloop()
