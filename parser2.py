from bs4 import BeautifulSoup
import requests
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_count_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    regularka = r'^pagination-item-\w{1,10}.pagination-item_arrow-\w{1,10}'
    pagination_item = ''
    try:
        # pagination_item = soup.find('span', class_=re.compile(regularka))
        pagination_item = soup.find('span', class_=re.compile(regularka)).previousSibling.previousSibling  # Fucking BS4
        print(pagination_item)
    except :
        print('suka blyat')
    # print(dir(pagination_item))
    # count_pages = int(pagination_item)

    return 100  # I am repairing this shit later


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['metro'],
                         data['url']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item__line')
    for ad in ads:
        try:
            title = ad.find('h3', class_='title item-description-title').find('a').text.strip()
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('h3', class_='title item-description-title').find('a').get('href')
        except:
            url = ''

        try:
            price = ad.find('span', class_='price price_highlight').text.strip()
        except:
            # price = ''
            price = ad.find('div', class_='about').text.strip()

        try:
            metro = ad.find('span', class_='item-address__string').text.strip()
        except:
            metro = ''

        data = {'title': title,
                'price': price,
                'metro': metro,
                'url': url}

        write_csv(data)


def main():
    url = 'https://www.avito.ru/rossiya/telefony?q=hts'
    base_url = 'https://www.avito.ru/rossiya/telefony?'
    page_part = 'p='
    query_part = 'q=htc'
    html = get_html(url)
    pages = get_count_pages(html)
    for i in range(1, 3):  # really - pages + 1
        url_gen = base_url + page_part + str(i) + '&' + query_part
        html = get_html(url_gen)
        get_page_data(html)




if __name__ == '__main__':
    print(main())
