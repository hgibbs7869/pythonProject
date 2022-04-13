# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random

def roll(sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled

def main():
    sides = 6
    rolling = True
    while rolling == 5000:
        roll_again = input("Roll again?")
        if roll_again.lower() !="q" or roll_again(sides)=> '':
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
        else:
        rolling = False
        print("Thanks for playing")
