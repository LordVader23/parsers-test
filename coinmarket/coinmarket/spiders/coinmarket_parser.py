# -*- coding: utf-8 -*-
import scrapy
import re


class CoinmarketParserSpider(scrapy.Spider):
    name = 'coinmarket_parser'
    allowed_domains = ['https://coinmarketcap.com/all/views/all/', 'coinmarketcap.com']
    start_urls = ['http://https://coinmarketcap.com/all/views/all//']

    def parse(self, response):
        names = response.css('div img + a.cmc-link::text').extract()
        symbols_dirty = response.css('td div::text').extract()
        symbols = []

        for symbol in symbols_dirty:
            # if re.compile('^[A-Z]{2,5}'):
            #     pass

        price_links = response.css('td a.cmc-link::text').extract()
        prices = []

        for price_link in price_links:
            # if re.compile('^'):
            #     prices.append(price_link)




