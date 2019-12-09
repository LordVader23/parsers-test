from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\py\geckodriver.exe')
        self.navigate()
        self.get_image()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def get_image(self):
        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location
        size = image.size

        self.crop(location, size)
        self.tel_recog()

    def tel_recog(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x + width, y + height)).save('tel.gif')

    def navigate(self):
        self.driver.get('https://www.avito.ru/barnaul/telefony/htc_desire_626g_978574960')

        button = self.driver.find_element_by_xpath('//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()

        sleep(3)

        self.take_screenshot()


def main():
    b = Bot()


if __name__ == '__main__':
    main()