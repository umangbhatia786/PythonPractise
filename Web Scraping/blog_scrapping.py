import requests
from bs4 import BeautifulSoup
from csv import writer

for page_num in range(1,7):
    page_url = f'https://www.rithmschool.com/blog?page={page_num}'
    response = requests.get(page_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')

    file_path = r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\Web Scraping\blog_data.csv'
    if page_num == 1:
        with open(file_path, 'w') as file:
            csv_writer = writer(file)
            csv_writer.writerow(['Title', 'URL', 'TimeStamp'])

            for article in articles:
                a_tag = article.find('a')
                title = a_tag.get_text()
                url = a_tag['href']
                article_time = article.find('time')['datetime']

                csv_writer.writerow([title, url, article_time])
    else:
        with open(file_path, 'a') as file:
            csv_writer = writer(file)
            for article in articles:
                a_tag = article.find('a')
                title = a_tag.get_text()
                url = a_tag['href']
                article_time = article.find('time')['datetime']

                csv_writer.writerow([title, url, article_time])
