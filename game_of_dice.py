# """
# Use data structures
#
# Game of dice
#
# Game play: to simulate the flipping coin
# To have a program to randomly select a side of the coin
#
# Give he user the ability ti guess ran
#
# """
import random

coin = ['h', 't']


y=0
z=0
while True:
    choice = input("enter h for Heads and t for tails and x to quit ")
    x = random.choice(coin)
    if (choice == 'h' or choice == 't' or choice == 'x'):
        if (choice == 'h' or choice == 't' ):
            if (x == choice):
                print('you won')
                y=y+1
            else:
                print('you lost')
                z = z + 1
        else:
            print('thanks for playing')
            print('you won', y, 'times')
            print('you lost', z, 'times')
            break
    else:
        print('wrong choice ,try again')

