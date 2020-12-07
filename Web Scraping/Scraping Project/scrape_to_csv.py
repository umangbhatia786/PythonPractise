import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from time import sleep
from random import choice

BASE_URL = 'http://quotes.toscrape.com'

CSV_PATH = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\Web Scraping\Scraping Project\quote_data.csv'

def scrape_quotes():
    all_quotes = []
    page = '/page/1/'
    while page:
        res = requests.get(f'{BASE_URL}{page}')
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all(class_ = 'quote')


        for quote in quotes:
            all_quotes.append({
                'Text'             : quote.find(class_ = 'text').get_text(),
                'Author'            : quote.find(class_ = 'author').get_text(),
                'Author Bio-Link'   : quote.find('a')['href']
            })

        next_btn = soup.find(class_ = 'next')
        page = next_btn.find('a')['href'] if next_btn else None
        print(page)
        #sleep(2)
    return all_quotes


def write_quotes(quotes):
    with open(CSV_PATH, 'w') as file:
        headers = ['Text', 'Author', 'Author Bio-Link']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()

        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)
