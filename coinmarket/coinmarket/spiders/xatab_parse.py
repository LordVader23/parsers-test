import scrapy


class XatabParseSpider(scrapy.Spider):
    name = 'xatab_parse'
    allowed_domains = ['v.otxataba.net']
    start_urls = ['https://v.otxataba.net/']
    custom_settings = {
        'FEED_URI': 'otxataba' + '.csv',
        'FEED_FORMAT': 'csv',
        # 'FEED_EXPORTERS': {
        #     'json': 'scrapy.exporters.JsonItemExporter',
        # },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }
    page_num = 1

    def parse(self, response):
        links = response.css("div.entry__title h2 > a::attr('href')").extract()
        num_of_pages = response.css("div.pagination span.nav_ext + a::attr('href')").extract()

        yield from response.follow_all(links, self.parse_page)

        if self.page_num < num_of_pages:
            page_url = r'https://v.otxataba.net/page/{}/'.format(self.page_num)
            XatabParseSpider.page_num += 1
            yield response.follow(page_url, callback=self.parse)


    def parse_page(self, response):
        pass

