from bs4 import BeautifulSoup
import re


def main():
    html = open('index.html').read()
    soup = BeautifulSoup(html, 'lxml')

    # div = soup.find('div', class_='links')
    # links = div.find_all('a')
    #
    # for a in links:
    #     link = a.get('href')
    #     print(link)

    # div = soup.find('h1').find_parent('div', class_='two')
    # print(div)

    # text = soup.find('h2').previous_sibling
    # print(text)
    div = soup.find('div', text=re.compile(r'^\d{2}.\d{2}.\d{4}$'))
    # url = a.get('href')
    print(div.next)



if __name__ == '__main__':
    main()
