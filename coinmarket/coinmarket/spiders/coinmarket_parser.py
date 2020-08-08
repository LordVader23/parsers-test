# -*- coding: utf-8 -*-
import scrapy
import re


class CoinmarketParserSpider(scrapy.Spider):
    name = 'coinmarket_parser'
    allowed_domains = [r'https://coinmarketcap.com/all/views/all/', 'coinmarketcap.com']
    start_urls = [r'https://coinmarketcap.com/all/views/all/']

    def parse(self, response):
        names = response.css('td a.cmc-link::text').extract()[0::3]
        symbols = response.css('td div::text').extract()[1::7]
        prices = response.css('td a.cmc-link::text').extract()[1::3]
        links = response.css("td a.cmc-link::attr('href')").extract()[1::3]

        row_data = zip(names, symbols, prices, links)

        for (name, symbol, price, link) in row_data:
            scrapped_data = {
                'page': response.url,
                'name': name,
                'price': price,
                'symbol': symbol,
                'link': r'https://coinmarketcap.com' + link,
            }

            yield scrapped_data

    def errback_web(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        item = {}
        item['Web Address'] = failure.request.url

        yield item





