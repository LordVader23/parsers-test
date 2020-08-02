from bs4 import BeautifulSoup
import re

regexp = r'^\d{2}.\d{2}.\d{4}$'

if __name__ == '__main__':
    html = open('index.html').read()
    soup = BeautifulSoup(html, 'lxml')

    # div = soup.find('div', {'class': 'links'})
    # print(div)

    # links = soup.find_all('a')
    # for a in links:
    #     print(a.get('href'))

    # div = soup.find('h1').find_parent('div', class_='two')
    # print(div)

    text = soup.find('h1').next_sibling
    print(text)

    div = soup.find('div', text=re.compile(regexp))
    print(div.next)


