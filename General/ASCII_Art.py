from pyfiglet import figlet_format
from termcolor import colored


def print_message(msg, input_color):
    '''The function to print a message with user-defind color'''

    if input_color not in valid_colors:
        input_color = 'magenta'

    ascii_art = figlet_format(msg)
    colored_ascii_art = colored(ascii_art, color=input_color)
    print(msg)


valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input('What would you like to print?\n')
input_color = input('What color would you like?\n')

print_message(msg, input_color)
