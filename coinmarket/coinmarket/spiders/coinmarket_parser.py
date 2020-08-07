# -*- coding: utf-8 -*-
import scrapy
import re


class CoinmarketParserSpider(scrapy.Spider):
    name = 'coinmarket_parser'
    allowed_domains = ['https://coinmarketcap.com/all/views/all/', 'coinmarketcap.com']
    start_urls = ['http://https://coinmarketcap.com/all/views/all//']

    def parse(self, response):
        # names = response.css('div img + a.cmc-link::text').extract()
        names = response.css('td a.cmc-link::text').extract()[0::3]
        symbols_dirty = response.css('td div::text').extract()
        # symbols = []
        symbols = response.css('td div::text').extract()[1::7]

        # for symbol in symbols_dirty:
        #     if re.compile('^[A-Z]{3,5}$').findall(symbol.strip()):
        #         symbols.append(symbol)

        price_links = response.css('td a.cmc-link::text').extract()
        price_hreves = response.css("td a.cmc-link::attr('href')").extract()
        prices = response.css('td a.cmc-link::text').extract()[1::3]
        links = response.css("td a.cmc-link::attr('href')").extract()[1::3]

        # for (index, (link, href)) in enumerate(zip(price_links, price_hreves)):
        #     if re.compile('^/currencies/').findall(href.strip()):
        #         prices.append(link)
        #         links.append('https://coinmarketcap.com/' + 'href')
        row_data = zip(names, symbols, prices, links)

        for (name, symbol, price, link) in row_data:
            scrapped_data = {
                'page': response.url,
                'name': name,
                'price': price,
                'link': link,
            }

            yield scrapped_data





