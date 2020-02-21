from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.links = 0  # Default value
        self.get_links()
        self.get_info()

    def get_links(self):
        self.driver.get('https://coinmarketcap.com/all/views/all/')

        sleep(5)

        links = self.driver.find_elements_by_xpath('//div[@class="cmc-table__column-name sc-1kxikfi-0 eTVhdN"]'
                                                   '/a[@class="cmc-link"]')
        links_ar = []

        for link in links:
            links_ar.append(link.get_attribute('href'))

        self.links = links_ar

    def write_csv(data):
        data_row = [
            data['title'],
            data['price'],
        ]
        with open('coin_market.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data_row)

    def get_info(self):
        info = []  # Array with dicts({title, price}) and buffer

        for link in self.links[0:10]:
            current_url = self.driver.current_url  # Save current link
            new_window_url = link

            self.driver.get(new_window_url)  # Follow link

            wait2 = WebDriverWait(self.driver, 10)
            wait2.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//div[@class="cmc-details-panel-header sc-1extin6-0 gMbCkP"]/h1')))

            title = self.driver.find_element_by_xpath('//div[@class="cmc-details-panel-header sc-1extin6-0 gMbCkP"]/h1').text
            price = self.driver.find_element_by_class_name('cmc-details-panel-price__price').text

            if len(info) == 10:  # if buffer info is fulled info will write in csv file
                for elem in info:
                    write_csv(elem)
                else:
                    del info[:]
            else:
                data = {'title': title,
                        'price': price}
                info.append(data)

            self.driver.get(current_url)  # Follow back


if __name__ == '__main__':
    bot = Bot()





