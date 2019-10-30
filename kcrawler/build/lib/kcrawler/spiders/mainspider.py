import scrapy
from kcrawler.items import KcrawlerItem


class MainSpider(scrapy.Spider):
    name = 'mainspider'

    def __init__(self, keyword=None, unique_id=None, *args, **kwargs):
        super(MainSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'https://vijaykarnataka.indiatimes.com/topics/%s' % keyword]

    def parse_item(self, response):
        item = KcrawlerItem()
        item["content"] = []
        listofarticles = response.css(
            'div.tab_content div.content span.title::text').getall()
        for i in listofarticles:
            item["content"].append(i)
        yield item
