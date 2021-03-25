# A simple program that changes the Finch buzzer based on x-axis orientation.
from finch import Finch
from random import randint
from time import sleep

# Instantiate the Finch object and connect to Finch
tweety = Finch()

left, right = tweety.obstacle()

i = 0
# Do the following while no obstacles are detected by Finch
while True:
    # Get the accelerations
    x, y, z, tap, shake = tweety.acceleration()
    # Print the acceleration data
    if (i % 50 == 0):
        print("X is %.2f, Y is %.2f" % (x, y,));
        print(tweety.temperature);
    # Make it buzz - beak up yields higher frequencies, beak down yields lower
    #tweety.buzzer(0.1, (880 - int(x*770.0)));

    # Get obstacles to use to exit loop
    left, right = tweety.obstacle()
    i += 1
    
tweety.close()
