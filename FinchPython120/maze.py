from time import sleep
from finch import Finch

fin = Finch()
left, right = fin.obstacle()
x = 1
while True:
    try:
        while True:
            fin.wheels(0.5, 0.5)
            sleep(0.5)
            if left and right:
                fin.wheels(-1, 0.5)
                sleep(0.9)
            else:
                fin.wheels(0.5, -1)
                sleep(0.9)

            while not left and not right:
                fin.wheels(0.5, 0.5)
                sleep(0.5)
                break
            if left or right:
                fin.wheels(-0.5, -0.5)
                sleep(0.5)
                fin.wheels(-1, -0.3)
                sleep(0.5)
    except:
        print('Error')
