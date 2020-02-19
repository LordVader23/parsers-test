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

        links = self.driver.find_elements_by_xpath('//a[@class="cmc-link"]')
        links_ar = []

        for link in links:
            links_ar.append(link.get_attribute('href'))

        self.links = links_ar

    def get_info(self):
        info = []  # Array with dicts({title, price})

        for link in self.links:
            current_url = self.driver.current_url  # Save current link
            new_window_url = link

            self.driver.get(new_window_url)  # Follow link

            wait2 = WebDriverWait(self.driver, 10)
            wait2.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//div[@class="cmc-details-panel-header sc-1extin6-0 gMbCkP"]/h1')))

            title = self.driver.find_element_by_xpath('//div[@class="cmc-details-panel-header sc-1extin6-0 gMbCkP"]/h1').text
            price = self.driver.find_element_by_class_name('cmc-details-panel-price__price').text

            data = {'title': title,
                    'price': price}
            info.append(data)

            self.driver.get(current_url)  # Follow back

        print(info)


if __name__ == '__main__':
    bot = Bot()





