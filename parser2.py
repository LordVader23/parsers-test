from bs4 import BeautifulSoup
import requests
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_count_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    regularka = r'^pagination-item-([A-Z0-9a-z]){1,5}\spagination-item_arrow-([A-Z0-9a-z]){1,5}$' # Regexp for the class_name of the elem
    pagination_item = ''
    try:
        # Find elem use class_name, which will change in future
        pagination_item = soup.find('span', class_=re.compile(regularka)).previousSibling
    except :
        print('suka blyat')
    count_pages = int(pagination_item.next)

    return count_pages


def write_csv(data):
    data_row = [
        data['title'],
        data['price'],
        data['metro'],
        data['url']
    ]
    with open('avito.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data_row)


def write_file(data):
    file = open(r'avito_file.txt', 'a', encoding='utf-8')
    data_l = [data[i] for i in data]
    data_row = ';'.join(data_l)
    data_row += '\n'
    # data_row = 'title - {}'.format(data['title'])
    file.write(data_row)


def get_page_data(html, to_path):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item__line')
    for ad in ads:
        try:
            title = ad.find('a', class_='snippet-link').text.strip()

            if ('htc' in title) or ('HTC' in title)\
                    or ('hts' in title) or ('HTS' in title):
                pass
            else:
                continue
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

        if to_path == 'file':
            write_file(data)
        else:
            write_csv(data)


def main(to_path='csv'):
    url = 'https://www.avito.ru/rossiya/telefony?q=hts'
    base_url = 'https://www.avito.ru/rossiya/telefony?'
    page_part = 'p='
    query_part = 'q=htc'
    html = get_html(url)
    pages = get_count_pages(html)
    for i in range(1, 3):  # really - pages + 1
        url_gen = base_url + page_part + str(i) + '&' + query_part
        html = get_html(url_gen)
        get_page_data(html, to_path)


if __name__ == '__main__':
    print(main())
