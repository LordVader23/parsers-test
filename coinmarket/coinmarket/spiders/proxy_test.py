from fake_useragent import UserAgent
import scrapy


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'
    allowed_domains = ['coinmarketcap.com']
    start_urls = [r'https://coinmarketcap.com/']

    def parse(self, response):
        yield response.follow(r'http://sitespy.ru/my-ip', callback=self.get_ip)

    def get_ip(self, response):
        ip = response.css('span.ip::text').extract()
        user_agent = response.css('span.ip + br + span')

