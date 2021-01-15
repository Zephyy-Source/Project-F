"""
Программа для отрисовки матричного графического интерфейса
для последующего движения Finch robot по заданным кнопкам
"""
import tkinter as tk
arr = []
prev_bt = 0


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
    else:  # обработка ошибки
        return

    return narr


def check_way(num: int, arr: list, bt: tk.Button) -> None:
    """
    Функция на основе информации полученной с gen_perm_num
    добавляет номер нажатой кнопки, или нет.
    """
    global prev_bt
    prev_bt = bt
    
    print(arr)
    print(prev_bt)
    try:
        prev_bt.config(bg="grey")
    except Exception:
        pass
    
    if len(arr) != 0:
        if 0 < num < 10 and arr[0] != num:
            carr = gen_perm_num(arr[len(arr) - 1])
            if num in carr:
                arr.append(num)
                bt.config(bg="blue")
                bt_prev = bt
            else:
                bt.config(bg="red")
                bt_prev = bt
                return
    else:
        arr.append(num)


def Draw_button() -> list:
    # Функция создания кнопок в графическом интерфейсе
    x, y = 10, 0
    for i in range(9):
        bt = tk.Button(heigh="5", width="5")
        bt.config(command=lambda i=i+1, arr=arr, bt=bt: check_way(i, arr, bt))
        bt.grid(column=x, row=y)
        y += 8 if x == 30 else 0
        x = 10 if x == 30 else x + 10



win = tk.Tk()
win.title("PyFinchMovement")
win.geometry("205x300")
# tabs = Draw_tabs(win)
Draw_button()
win.mainloop()
print(arr)
