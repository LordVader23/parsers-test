import requests
from bs4 import BeautifulSoup as bs
import csv
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def get_links(html):
    """
    Get all links from page(with url=html) and returns array with them.
    :param html: url
    :return: array with links(strs)
    """
    soup = bs(html, 'lxml')
    all_rows = soup.find_all('td', class_=re.compile(r'^cmc-table__cell'))
    all_links = []

    for row in all_rows:
        link = row.find('a', href=re.compile(r'^/currencies/[a-z, A-Z]+/$'))
        if link:
            url = 'https://coinmarketcap.com' + link.get('href')
            all_links.append(url)


    # links = soup.find_all('a', class_='cmc-link', href=re.compile(r'^/currencies/'))
    # all_links = []
    #
    # for link in links:
    #     url = 'https://coinmarketcap.com' + link.get('href')
    #     all_links.append(url)

    return all_links





if __name__ == '__main__':
    url = 'https://coinmarketcap.com/all/views/all/'
    html = get_html(url)
    all_links = get_links(html)

    for link in all_links:
        print(link)