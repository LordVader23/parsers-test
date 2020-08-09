import scrapy


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'
    allowed_domains = ['coinmarketcap.com']
    start_urls = [r'https://coinmarketcap.com/']

    def parse(self, response):
        pass
