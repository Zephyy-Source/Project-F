from time import sleep
from finch import Finch
from threading import Thread

fin = Finch()
lobs, robs = fin.obstacle()


def obstacle():
    while True:
        global lobs, robs
        lobs, robs = fin.obstacle()
        print(lobs)
        print(robs)
        sleep(0.5)


th1 = Thread(target=obstacle)
th1.start()

while True:
    try:
        while True:
            fin.wheels(0.5, 0.5)
            sleep(0.5)
            if lobs or robs():
                fin.wheels(-1, -0.1)
                sleep(0.5)
            else:
                fin.wheels(0.5, -1)
                sleep(0.5)
            while not lobs or not robs:
                fin.wheels(0.5, 0.5)
                sleep(0.5)
                break
            if lobs or robs:
                fin.wheels(-0.5, -0.5)
                sleep(0.5)
                fin.wheels(-1, -0.3)
                sleep(0.5)
    except:
        print('error')