import random

def computer_guess_game():
    try:
        x = int(input('Enter a maximum number: '))
    except ValueError:
        print('Invalid input! ')
