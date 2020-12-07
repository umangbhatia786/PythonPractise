from random import randint


while True:
    comp_choice = randint(1, 10)
    user_choice = int(input('Guess a number between 1 and 10: '))

    if user_choice > comp_choice:
        print('Your guess is too high')
    elif user_choice < comp_choice:
        print('Your guess is too low')
    else:

        print('You guessed it! You finally won')
        is_continue = input('Do you want to continue playing (Y/N): ')

        if is_continue == 'N':
            print('Thank you for playing!')
            break
        else:
            comp_choice = randint(1, 10)
            user_choice = None
