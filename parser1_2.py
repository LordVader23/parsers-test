import requests
from bs4 import BeautifulSoup as bs
import csv
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def get_links(html):
    soup = bs(html, 'lxml')
    # all_rows = soup.find_all('td', class_=re.compile(r'^cmc-table__cell'))
    # all_links = []
    #
    # for row in all_rows:
    #     link = row.find('a', href=re.compile(r'^/currencies/'))
    #     if link:
    #         url = 'https://coinmarketcap.com' + link.get('href')
    #         all_links.append(url)
    links = soup.find_all('a', class_='cmc-link')
    all_links = []

    for link in links:
        url = 'https://coinmarketcap.com' + link.get('href')
        all_links.append(url)

    return all_links





if __name__ == '__main__':
    pass