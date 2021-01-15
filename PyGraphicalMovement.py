"""
Программа для отрисовки матричного графического интерфейса
для последующего движения Finch robot по заданным кнопкам
"""
import tkinter as tk
arr = []


def gen_perm_num(num):
    if num == 5:
        narr = [x for x in range(1, 10) if x != 5]
    elif num in (1, 3, 7, 9):
        x = num - 1 if not num % 3 else num + 1
        narr.append(x)
        y = num + 3 if num < 5 else num - 3
        narr.append(y)

    return narr


def check_way(num: int, arr: list) -> list:
    if len(arr) != 0:
        if 0 < num < 10 and arr[0] != num:
            carr = gen_perm_num(arr[len(arr) - 1])
            if num in carr:
                arr.append(num)
            else:
                return
    else:
        arr.append(num)


def Draw_button() -> list:
    # Функция создания кнопок в графическом интерфейсе
    x, y = 10, 0
    barr = []
    for i in range(9):
        barr.append(tk.Button(heigh="5", width="5",
                              command=lambda i=i+1, arr=arr: arr.append(i)))
        print(i)
        barr[i].grid(column=x, row=y)
        y += 8 if x == 30 else 0
        x = 10 if x == 30 else x + 10
        print(x, y)
    return barr


win = tk.Tk()
win.title("PyFinchMovement")
win.geometry("205x300")
# tabs = Draw_tabs(win)
buttons = Draw_button()
win.mainloop()
print(arr)
