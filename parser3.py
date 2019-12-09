from selenium import webdriver


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\py\geckodriver.exe')
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def navigate(self):
        self.driver.get('https://www.avito.ru/barnaul/telefony/htc_desire_626g_978574960')

        button = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()

        self.take_screenshot()


def main():
    b = Bot()


if __name__ == '__main__':
    main()