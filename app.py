import random

roll_min = 1
roll_max = 6
number_of_dice_input = input("Enter number of dice to roll between 1 and 5: ")
number_of_dice = int(number_of_dice_input)
dice_arr = []


def ran_num():
    return random.randint(roll_min, roll_max)


def roll_dice():
    i = 0
    del dice_arr[:]

    while i < number_of_dice:
        dice_arr.append(ran_num())
        i += 1

    show_dice()


def show_dice():
    print(dice_arr)
    roll_again = input('Roll agian? (Y)es, (N)o or (R)estart: ')

    if roll_again.upper() == "Y":
        roll_dice()
    elif roll_again.upper() == "N":
        print("Thanks for playing!")
    elif roll_again.upper() == "R":
        dice_num = input("Enter number of dice to roll between 1 and 5: ")
        global number_of_dice
        number_of_dice = int(dice_num)
        roll_dice()


if number_of_dice <= 0 or number_of_dice > 5:
    reenter = input("Please enter a number between 1 and 5: ")
    number_of_dice = int(reenter)
    roll_dice()
else:
    roll_dice()
