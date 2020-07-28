from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    html = open('index.html').read()
    soup = BeautifulSoup(html, 'lxml')

