import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import html5lib


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


def get_data(html):
    """
    Gets name and price from the page(url=html)
    :param html: url
    :return: dict with keys: name(str), price(int)
    """
    soup = bs(html, 'html5lib')

    data = {}
    # name = soup.find('img', class_='cmc-static-icon cmc-static-icon-1')
    try:
        name = soup.find('img', alt='Bitcoin').next_sibling.strip()
    except:
        name = ''
    data['name'] = name

    try:
        price = soup.find('span', class_='cmc-details-panel-price__price').text
        price = price.replace('\xa0', ' ')
    except:
        price = ''
    data['price'] = price

    return data


if __name__ == '__main__':
    url = 'https://coinmarketcap.com/all/views/all/'
    html = get_html(url)
    all_links = get_links(html)

    # file = open('test_html.html', 'w')
    # file.write(get_html(all_links[0]))
    # file.close()

    # for link in all_links:
    #     print(link)
    # print(all_links[0])
    file = open('btc.html', 'r').read()
    # print(get_data(get_html(all_links[0])))
    print(get_data(file))

