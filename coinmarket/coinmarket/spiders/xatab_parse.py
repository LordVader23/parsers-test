import scrapy
import re
import time
import random


class XatabParseSpider(scrapy.Spider):
    name = 'xatab_parse'
    allowed_domains = ['v.otxataba.net']
    start_urls = ['https://v.otxataba.net/']
    custom_settings = {
        'FEED_URI': 'otxataba_1' + '.csv',
        'FEED_FORMAT': 'csv',
        # 'FEED_EXPORTERS': {
        #     'json': 'scrapy.exporters.JsonItemExporter',
        # },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }
    page_num = 1  # to save number of page
    num_of_pages = 0  # to save number of pages

    def parse(self, response):
        headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
        links = response.css("div.entry div a::attr('href')").extract()
        links = list(set(links))  # To delete the same lines

        for link in links:
            if re.search(r'#download$', link):
                continue
            else:
                t = random.uniform(1, 3)
                time.sleep(t)
                yield response.follow(link, self.parse_page)
                # yield scrapy.Request(link, headers=headers, callback=self.parse_page)
        if not self.num_of_pages:
            XatabParseSpider.num_of_pages = int(response.css("div.pagination span.nav_ext + a::text").extract()[0])

        if self.page_num < 15:
            XatabParseSpider.page_num += 1
            page_url = r'https://v.otxataba.net/page/{}/'.format(self.page_num)
            yield response.follow(page_url, callback=self.parse)

    def parse_page(self, response):
        title = response.css("div.inner-entry__allinfo h1.inner-entry__title::text").extract()[0]
        year_of_issue = response.css("div.inner-entry__details::text").extract()[1].strip()
        genres_dirty = response.css("div.inner-entry__details a::text").extract()
        genres = []

        for elem in genres_dirty:
            if re.search(r'\d+ года', elem.strip()):
                continue
            elif elem.strip() == 'Лицензии' or elem.strip() == 'Ожидаемые':
                continue
            else:
                genres.append(elem)

        some_string = response.css("div.inner-entry__details").extract()[0]  # Some shit to extract developer string(it works!)
        developer = re.search(r'Разработчик: </strong> (.+)<br>', some_string).group(1)
        try:
            download_link = response.css(r"div[id='download'] a::attr('href')").extract()[0]
        except IndexError:
            pass
        else:
            yield {
                'page': response.url,
                'title': title,
                'year of issue': year_of_issue,
                'genres': r'/'.join(genres),
                'developer': developer,
                'download link': download_link,
            }

    # def start_requests(self):
    #     request = scrapy.Request('https://www.hidemyass-freeproxy.com/proxy/ru-ua/aHR0cHM6Ly92Lm90eGF0YWJhLm5ldC8', callback=self.parse_page)
    #     # request.meta['proxy'] = 'http://198.51.100.14:8080'
    #     request.headers['Connection'] = 'keep-alive'
    #     return request


