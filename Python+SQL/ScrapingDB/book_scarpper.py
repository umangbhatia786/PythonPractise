import sqlite3
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    '''Function To Scrape Books Details and Insert into DB'''
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    books = soup.find_all(class_ = 'product_pod')
    all_books = []

    for book in books:
        book_data = get_title(book), get_price(book), get_rating(book)
        all_books.append(book_data)

    save_books(all_books)

def get_title(book):
    return book.find('h3').find('a')['title']

def get_price(book):
    return float(book.select('.price_color')[0].get_text()[2:])

def get_rating(book):
    ratings_dict = {
    'Zero': 0,
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
    }
    rating = book.select('.star-rating')[0].get_attribute_list('class')[-1]
    return ratings_dict[rating]

def save_books(books_list):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE books (Title TEXT, Price REAL, Rating INTEGER);''')
    template_query = f"INSERT INTO books VALUES (?,?,?)"
    c.executemany(template_query, books_list)
    conn.commit()
    conn.close()

scrape_url = "https://books.toscrape.com/"
    
'''Finally Calling the Scrape Books Method'''
scrape_books(scrape_url)


