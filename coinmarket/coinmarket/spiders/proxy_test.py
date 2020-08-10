from fake_useragent import UserAgent
from random import choice
import scrapy
import datetime


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'
    allowed_domains = ['coinmarketcap.com']
    # start_urls = [r'https://coinmarketcap.com/']
    start_urls = [r'http://sitespy.ru/my-ip']
    custom_settings = {
        'FEED_URI': 'proxy_test' + datetime.datetime.today().strftime('%y%m%d') + '.csv',
        'FEED_FORMAT': 'csv',
        # 'FEED_EXPORTERS': {
        #     'json': 'scrapy.exporters.JsonItemExporter',
        # },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        # yield response.follow(r'http://sitespy.ru/my-ip', callback=self.get_ip)
        ip = response.css('span.ip::text').extract()
        user_agent = response.css('span.ip + br + span::text').extract()

        yield {
            'ip': ip,
            'user_agent': user_agent,
        }

    def get_ip(self, response):
        ip = response.css('span.ip::text').extract()
        user_agent = response.css('span.ip + br + span')
        print(ip)
        print(user_agent)

