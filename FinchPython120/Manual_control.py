from finch import Finch
import keyboard
import time

finch = Finch()
gear = 1
print(gear)

while True:
    try:


# FIRST GEAR
        while gear == 1:
            if keyboard.is_pressed('w'):
                finch.wheels(0.3, 0.3)
            if keyboard.is_pressed('a'):
                finch.wheels(0, 0.3)
            if keyboard.is_pressed('d'):
                finch.wheels(0.3, 0)
            if keyboard.is_pressed('shift'):
                gear += 1
                time.sleep(0.5)
                print(gear)
            if keyboard.is_pressed('ctrl'):
                gear -= 1
                time.sleep(0.5)
                print(gear)
            finch.wheels(0, 0)

# SECOND GEAR
        while gear == 2:
            if keyboard.is_pressed('w'):
                finch.wheels(0.6, 0.6)
            if keyboard.is_pressed('a'):
                finch.wheels(0, 0.6)
            if keyboard.is_pressed('d'):
                finch.wheels(0.6, 0)
            if keyboard.is_pressed('shift'):
                gear += 1
                time.sleep(0.5)
                print(gear)
            if keyboard.is_pressed('ctrl'):
                gear -= 1
                time.sleep(0.5)
                print(gear)
            finch.wheels(0, 0)

    # THIRD GEAR
        while gear == 3:
            if keyboard.is_pressed('w'):
                finch.wheels(1, 1)
            if keyboard.is_pressed('a'):
                finch.wheels(0, 1)
            if keyboard.is_pressed('d'):
                finch.wheels(1, 0)
            if keyboard.is_pressed('ctrl'):
                gear -= 1
                time.sleep(0.5)
                print(gear)
            finch.wheels(0, 0)

# REVERSE GEAR
        while gear == 0:
            if keyboard.is_pressed('s'):
                finch.wheels(-1, -1)
            if keyboard.is_pressed('d'):
                finch.wheels(-1, 0)
            if keyboard.is_pressed('a'):
                finch.wheels(0, -1)
            if keyboard.is_pressed('shift'):
                gear +=1
                time.sleep(0.5)
                print(gear)
            finch.wheels(0, 0)
    except:
        print('Error')