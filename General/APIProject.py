from pyfiglet import figlet_format
from termcolor import colored
from random import choice
import requests


def print_message(msg, input_color):
    '''The function to print a message with user-defind color'''

    valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    if input_color not in valid_colors:
        input_color = 'magenta'

    ascii_art = figlet_format(msg)
    colored_ascii_art = colored(ascii_art, color=input_color)
    print(msg)

print_message('DAD JOKES 3000', 'blue')

user_input = input('What would you like to search for? ')

api_url = 'https://icanhazdadjoke.com/search'
res = requests.get(
    api_url, 
    headers = {'Accept': 'application/json'},
    params = {'term': user_input}
    ).json()

num_jokes = res['total_jokes']

if num_jokes > 1:
    print(f'There are {num_jokes} for this search term')
    print('A random joke from the search list is as below: ')
    print(choice(res['results'])['joke'])
elif num_jokes == 1:
    print('There is only one joke for this one!')
    print(res['results'][0]['joke'])
else:
    print(f'Sorry! There are no jokes for Search Term: {user_input}')



