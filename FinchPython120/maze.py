from time import sleep
from finch import Finch
import time
fin = Finch()
left, right = fin.obstacle()
def check():
    while not left and not right:
        fin.wheels(0.5,0.5)
        sleep(1)
    if left and right:
        fin.wheels(0.5, 0.5)
        sleep(1)
        fin.wheels(-1,-0.5)
        sleep(0.5)
    else:
        fin.wheels(1,0.5)
        sleep(0.5)
while True:
    fin.wheels(0.5,0.5)
    sleep(1)
    fin.wheels(1,0.3)
    sleep(0.5)
    check()
