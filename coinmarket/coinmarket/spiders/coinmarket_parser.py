# -*- coding: utf-8 -*-
import scrapy


class CoinmarketParserSpider(scrapy.Spider):
    name = 'coinmarket_parser'
    allowed_domains = ['https://coinmarketcap.com/all/views/all/', 'coinmarketcap.com']
    start_urls = ['http://https://coinmarketcap.com/all/views/all//']

    def parse(self, response):
        name = response.css('div img + a.cmc-link').extract()
