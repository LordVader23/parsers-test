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
            if re.compile('^[A-Z]{3,5}$').findall(symbol.strip()):
                symbols.append(symbol)

        price_links = response.css('td a.cmc-link::text').extract()
        price_hreves = response.css("td a.cmc-link::attr('href')").extract()
        prices = []
        links = []

        for (index, (link, href)) in enumerate(zip(price_links, price_hreves)):
            if re.compile('^/currencies/').findall(href.strip()):
                prices.append(link)
                links.append('https://coinmarketcap.com/' + 'href')




