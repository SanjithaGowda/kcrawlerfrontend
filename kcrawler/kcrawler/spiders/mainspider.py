import scrapy
from kcrawler.items import KcrawlerItem


class MainSpider(scrapy.Spider):
    name = 'mainspider'

    def __init__(self, *args, **kwargs):
        self.keyword = kwargs.get('keyword')
        self.unique_id = kwargs.get('uid')
        self.start_urls = [
            'https://vijaykarnataka.indiatimes.com/topics/%s' % self.keyword]
        super(MainSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = KcrawlerItem()
        listofarticles = response.css(
            'div.tab_content li.article div.content span.title::text').extract() + response.css('div.tab_content li.video div.content img::attr(title)').extract() 
        # listofarticles = response.css(
        #     'div.tab_content li.article div.content span.title::text , div.tab_content li.video div.content img::attr(title)').extract() 
        listofurls = response.css(
            'div.tab_content li.article div.content a::attr(href)').extract() +response.css('div.tab_content li.video div.content a::attr(href)').extract()
        listofcontents = response.css(
            'div.tab_content li.article div.content p::text').extract() +response.css('div.tab_content li.video div.content img::attr(title)').extract()
        for i in range(len(listofarticles)):
            item['url'] = 'https://vijaykarnataka.com' + listofurls[i]
            item['content'] = listofcontents[i]
            item["headline"] = listofarticles[i]
            yield item
