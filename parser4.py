from selenium import webdriver


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\py\geckodriver.exe')
        self.links = null  # Default value
        self.get_links()

    def get_links(self):
        self.driver.get('https://coinmarketcap.com/all/views/all/')

        links = self.driver.find_elements_by_xpath('//a[@class="cmc-link"]')
        links_ar = [link for link in links]
        self.links = links_ar

    def get_info(self):
        pass

