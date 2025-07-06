import random

def computer_guess_game():
    while True:
        try:
            x = int(input('Enter a maximum number: '))
            break
        except ValueError:
            print('Invalid input! ')

    low = 1
    high = x
    feedback = ''
    attempts = 0
    while feedback != 'c':
        if low > high:
            print('Your answers have caused a contradiction ')
            print('Please give honest feedback ')
            return
        computer_guess = random.randint(low , high)
        print(f'Computer guessed {computer_guess}')
        feedback = input('Is it too high (H), too low (L), or correct (C): ').lower().strip()
        attempts +=1
        print('Tries: ',attempts)
        
        if feedback == 'h':
            high = computer_guess - 1 
        elif feedback == 'l':
            low = computer_guess + 1
    print(f'The computer guessed your number {computer_guess} correctly!! ')


while True:
    computer_guess_game()
    restart = input('Do you want to play again?: (Y/N) ').lower().strip()
    if restart != 'y':
        print('Bye! See you soon')
        break