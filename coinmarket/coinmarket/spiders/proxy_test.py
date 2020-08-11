from fake_useragent import UserAgent
from random import choice
import scrapy
import datetime


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'
    allowed_domains = ['coinmarketcap.com']
    start_urls = [r'https://coinmarketcap.com/']
    # start_urls = [r'http://sitespy.ru/my-ip']
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
        # ip = response.css('span.ip::text').extract()
        # user_agent = response.css('span.ip + br + span::text').extract()
        #
        # yield {
        #     'ip': ip,
        #     'user_agent': user_agent,
        # }

        names = response.css('td a.cmc-link::text').extract()[0::3]
        symbols = response.css('td div::text').extract()[1::7]
        prices = response.css('td a.cmc-link::text').extract()[1::3]
        links = response.css("td a.cmc-link::attr('href')").extract()[1::3]
        yield scrapy.Request(r'http://sitespy.ru/my-ip', callback=self.get_ip, dont_filter=True)

        row_data = zip(names, symbols, prices, links)

        for (name, symbol, price, link) in row_data:
            scrapped_data = {
                'page': response.url,
                'name': name,
                'price': price,
                'symbol': symbol,
                'link': r'https://coinmarketcap.com{}'.format(link),
                # 'ip': ip,
                # 'user agent': ua,
            }

            yield scrapped_data

    def get_ip(self, response):
        ip = response.css('span.ip::text').extract()
        user_agent = response.css('span.ip + br + span::text').extract()

        yield ip, user_agent


