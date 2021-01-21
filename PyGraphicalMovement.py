"""
Программа для отрисовки матричного графического интерфейса
для последующего движения Finch robot по заданным кнопкам
"""
import tkinter as tk
import time
from tkinter import messagebox
from finch import Finch

arr = [5]

def Move_right(finch: Finch) -> None:
    "Функция, осуществяющая поворот вправо."
    finch.wheels(0.5, -0.5)
    time.sleep(0.6)
    finch.wheels(1, 1)
    time.sleep(0.5)
    finch.wheels(-0.5, 0.5)
    time.sleep(0.6)
    finch.wheels(0, 0)
    time.sleep(0.5)


def Move_left(finch: Finch) -> None:
    "Функция, осуществляющая поворот влево"
    finch.wheels(-0.5, 0.5)
    time.sleep(0.6)
    finch.wheels(1, 1)
    time.sleep(0.5)
    finch.wheels(0.5, -0.5)
    time.sleep(0.6)
    finch.wheels(0, 0)
    time.sleep(0.5)

def Move_forward(finch: Finch) -> None:
    "Функция, движения вперёд."
    finch.wheels(1, 1)
    time.sleep(0.5)
    finch.wheels(0, 0)
    time.sleep(0.5)

def Move_backward(finch: Finch) -> None:
    "Функция движения назад."
    finch.wheels(-0.8, 0.8)
    time.sleep(0.6)
    finch.wheels(1, 1)
    time.sleep(0.5)
    finch.wheels(0.8, -0.8)
    time.sleep(0.6)
    finch.wheels(0, 0)
    time.sleep(0.5)


def gen_prem_dest(From: int, to: int) -> str:
    "Генерирования возможного движения."
    dest = None
    if From == 5:
        if to == 2:
            dest = 'back'
        elif to == 4:
            dest = 'right'
        elif to == 6:
            dest = 'left'
        elif to == 8:
            dest = 'forw'
    elif From in (1, 7):
        if From + 1 == to:
            dest = 'left'
        else:
            dest = 'forw' if From == 1 else 'back'
    elif From in (3, 9):
        dest = 'right' if From - 1 == to else 'back'
        if From - 1 == to:
            dest = 'right'
        else:
            dest = 'forw' if From == 3 else 'back'
    elif From in (2, 8):
        if to == 5 and From == 2:
            dest = 'forw'
        elif to == 5 and From == 8:
            dest = 'back'
        elif From > to:
            dest = 'right'
        else:
            dest = 'left'
    elif From in (4, 6):
        if to == 5 and From == 6:
            dest = 'right'
        elif to == 5 and From == 4:
            dest = 'left'
        elif From > to:
            dest = 'back'
        else:
            dest = 'forw'
    return dest


def gen_move_arr(carr:list, farr: list):
    "Сгенерировать массим движения."
    if len(carr) <= 1:
        return
    else:
        farr.append(gen_prem_dest(carr[0], carr[1]))
        gen_move_arr(carr[1:], farr)
    
    
def Start_finch() -> None:
    "Коллбек, осуществляющий работу Finch Robot"
    try:
        finch = Finch()
        darr = []
        gen_move_arr(arr, darr)
        for i in darr:
            if i == 'right':
                Move_right(finch)
            elif i == 'left':
                Move_left(finch)
            elif i == 'back':
                Move_backward(finch)
            elif i == 'forw':
                Move_forward(finch)

            arr.clear()
    except Exception:
        messagebox.showerror("Ошибка", "Не полчилось подключиться к Finch robot")

        
def gen_perm_num(num: int) -> list:
    """
    Функция проверки может ли робот проехать в ячейку матрицы

    Проверка нужна так как робот не может двигаться по диагонали
    в данной реализации
    """
    narr = []
    if num == 5:
        narr = [2, 4, 6, 8]
    elif num in (1, 3, 7, 9):
        x = num - 1 if not num % 3 else num + 1
        narr.append(x)
        y = num + 3 if num < 5 else num - 3
        narr.append(y)
    elif num in (2, 8):
        narr = [num - 1, 5, num + 1]
    elif num in (4, 6):
        narr = [num - 3, 5, num + 3]

    return narr


def check_way(num: int, arr: list, text: tk.Label) -> None:
    """
    Функция на основе информации полученной с gen_perm_num
    добавляет номер нажатой кнопки, или нет.
    """
    if len(arr) == 0:
        arr.append(5)

    if 0 < num < 10:
        carr = gen_perm_num(arr[len(arr) - 1])

        if num in carr:
            marr = gen_perm_num(num)
            mess = "Вы находитесь в ячейке [{}]\nВозможный путь {}".format(
                num, marr)
            arr.append(num)
            text.config(text=mess)
        else:
            return
    # print(arr)  # Debugg


def Draw_elements(win: tk.Tk) -> None:
    start_msg = "Вы находитесь в ячейке [5]\nВозможный путь [2 4 6 8]"
    txt = tk.Label(win, text=start_msg, width="27", relief=tk.GROOVE, bg='white')
    txt.place(relx=0.0, rely=0.9)

    x, y = 1, 0
    for i in range(9):
        tk.Button(win, heigh="5", width="5", bg='white', text=i+1,
                  relief=tk.GROOVE,
                  command=lambda i=i+1:
                  check_way(i, arr, txt)).grid(column=x, row=y)
        y += 1 if x == 3 else 0
        x = 1 if x == 3 else x + 1

    tk.Button(win, width="23", text='Start', bg='deep sky blue',
              relief=tk.GROOVE,
              command=Start_finch).place(x=0, y=240)  


root = tk.Tk()
root.title("PyFinchMovement")
root.geometry("190x300")
Draw_elements(root)
root.resizable(0, 0)
root.mainloop()
print(arr)
