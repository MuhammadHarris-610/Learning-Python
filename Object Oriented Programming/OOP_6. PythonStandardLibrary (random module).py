# OOP: Exercise 6 (Using Modules from Python Standard Library)
# Program Description: Making a dice rolling program using the random module

from random import randint

class Die:
    def roll_die(sides=6):
        print(f"Sides: {sides}\nNumber: {randint(1, sides)}\n")

def main():
    my_dice = Die 
    print("Enter the number of sides of the Dice or Enter 'q' to quit.")
    while True:
        sides_no = input("Enter Sides: ")
        if sides_no.lower() == 'q':
            break
        else:
            my_dice.roll_die(int(sides_no))

main()