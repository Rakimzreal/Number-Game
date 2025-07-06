import random

def computer_guess_game():
    try:
        x = int(input('Enter a maximum number: '))
    except ValueError:
        print('Invalid input! ')

    low = 1
    high = x
    feedback = ''
    attempts = 0
    while feedback != 'c':
        computer_guess = random.randint(low , high)
        print(f'Computer guessed {computer_guess}')
        feedback = input('Is it too high (H), too low (L), or correct (C): ').lower().strip()
        attempts +=1
        print('Tries: ',attempts)
        
    