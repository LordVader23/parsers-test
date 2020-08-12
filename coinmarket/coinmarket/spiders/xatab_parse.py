import scrapy
import re


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
    page_num = 1  # to save number of page

    def parse(self, response):
        links = response.css("div.entry div a::attr('href')").extract()
        links = list(set(links))  # To delete the same lines

        for link in links:
            if re.search(r'#download$', link):
                continue
            else:
                yield response.follow(link, self.parse_page)

        num_of_pages = int(response.css("div.pagination span.nav_ext + a::text").extract()[0])
        # yield from response.follow_all(links, self.parse_page)
        # for link in links:
        #     yield from response.follow(link, self.parse_page)

        # if self.page_num < num_of_pages:
        #     page_url = r'https://v.otxataba.net/page/{}/'.format(self.page_num)
        #     XatabParseSpider.page_num += 1
        #     yield response.follow(page_url, callback=self.parse)

    def parse_page(self, response):
        title = response.css("div.inner-entry__allinfo h1.inner-entry__title::text").extract()[0]
        year_of_issue = response.css("div.inner-entry__details::text").extract()[1].strip()
        genres = response.css("div.inner-entry__details a::text").extract()

        for (index, elem) in enumerate(genres):
            if re.search(r'года$', elem.strip()):
                del genres[index]
            elif elem.strip() == 'Лицензии' or elem.strip() == 'Ожидаемые':
                del genres[index]

        some_string = response.css("div.inner-entry__details").extract()[0]  # Some shit to extract developer string(it works!)
        developer = re.search(r'Разработчик: </strong> (.+)<br>', some_string).group(1)
        download_link = response.css(r"div[id='download'] a::attr('href')").extract()[0]

        yield {
            'page': response.url,
            'title': title,
            'year of issue': year_of_issue,
            'genres': r'/'.join(genres),
            'developer': developer,
            'download link': download_link,
        }


