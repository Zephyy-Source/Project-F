from finch import Finch
import time
F = Finch()


F.wheels(0.5, -0.5)
time.sleep(0.6)
F.wheels(1, 1)
time.sleep(0.5)
F.wheels(-0.5, 0.5)
time.sleep(0.6)


