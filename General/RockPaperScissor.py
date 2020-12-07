from random import choice
def no_cheating_banner():
    for i in range(20):
        print('***** NO CHEATING *****')

for i in range(5):
    count_player = 0
    count_computer = 0

    print('...rock...\n...paper...\n...scissors')
    while True:
        player_choice = input('Enter Player one\'s choice: ')

        if player_choice in ['Rock', 'Paper', 'Scissor']:
            break
        else:
            print('Invalid Choice! Enter again')

    no_cheating_banner()
    computer_choice = choice(['Rock' , 'Paper', 'Scissor'])

    print('SHOOT!')

    if player_choice == computer_choice:
        print('It\'s a Tie')

    elif player_choice == 'Rock':
        if computer_choice == 'Paper':
            count_computer += 1
            print('You lost! Computer has Paper')

        else:
            count_player +=1
            print('You won! Computer has Scissor')

    elif player_choice == 'Paper':
        if computer_choice == 'Scissors':
            count_computer += 1
            print('You lost! Computer has Scissors')

        else:
            count_player +=1
            print('You won! Computer has Rock')

    elif player_choice == 'Scissor':
        if computer_choice == 'Rock':
            count_computer +=1
            print('You lost! Computer has Rock')

        else:
            count_player += 1
            print('You won! Computer has Paper')

if count_computer > count_player:
    print('Computer won the overall series')
elif count_player > count_computer:
    print('Player won the overall series!')
else:
    print('It\s a Tie!')