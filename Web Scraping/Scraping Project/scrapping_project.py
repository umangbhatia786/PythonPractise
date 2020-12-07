from typing import Dict
import requests
from bs4 import BeautifulSoup
from csv import DictReader
from time import sleep
from random import choice

CSV_DATA_PATH = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\Web Scraping\Scraping Project\quote_data.csv'
BASE_URL = 'http://quotes.toscrape.com'

def read_quote_data(file_path):
        with open(file_path) as file:
            csv_reader = DictReader(file)
            return list(csv_reader)


def start_game(all_quotes):

    random_quote = choice(all_quotes)
    remaining_guesses = 4
    guess = ''
    print('Here\'s a quote: ')
    print(random_quote['Text'])

    while guess.lower() != random_quote['Author'].lower():
        guess = input(f'Who said this quote? Guesses Remaining : {remaining_guesses}\n')
        remaining_guesses -=1

        if guess.lower() == random_quote['Author'].lower():
            print('Yay! You got it right')
            break
        
        if remaining_guesses == 3:
            author_page_res = requests.get('{}{}'.format(BASE_URL, random_quote['Author Bio-Link']))
            author_soup = BeautifulSoup(author_page_res.text, 'html.parser')

            author_born_date = author_soup.find(class_ = 'author-born-date').get_text()
            author_born_location = author_soup.find(class_ = 'author-born-location').get_text()
            print(f'The author was born on {author_born_date} {author_born_location}')
        
        elif remaining_guesses == 2:
            print('Here\'s a Hint: Author\'s First Name starts with {}'.format(random_quote['Author'][0]))

        elif remaining_guesses == 1:
            print('Here\'s a Hint: Author\'s Last Name starts with {}'.format(random_quote['Author'].split(' ')[1][0]))
        
        else:
            print('Sorry you ran out of guesses')
            print('The Correct Answer is {}'.format(random_quote['Author']))
    
    again = ''
    while again not in ('y', 'n', 'yes', 'no'):
        again = input('Would You like to play again? (y/n): ')

    if again.lower() in ('y', 'yes'):
        return start_game(all_quotes)
    else:
        print('Ok Goodbye!!')


quotes = read_quote_data(CSV_DATA_PATH)
start_game(quotes)