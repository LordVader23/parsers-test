import scrapy


class XatabParseSpider(scrapy.Spider):
    name = 'xatab_parse'
    allowed_domains = ['v.otxataba.net']
    start_urls = ['https://v.otxataba.net/']

    def parse(self, response):
        pass
