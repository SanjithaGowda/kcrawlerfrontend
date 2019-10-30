# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from main.models import EntryItem, ArticleItem
import json

class KcrawlerPipeline(object):
    def __init__(self, uid, *args, **kwargs):
        self.uniqueId = uid

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            keyword = crawler.settings.get('keyword'),
            uid=crawler.settings.get('uid'), 
        )

    def close_spider(self, spider):
        if(EntryItem.objects.filter(pk=spider.unique_id).exists()):
            EntryItem.objects.filter(pk=spider.unique_id).update(status='done')
    
    def process_item(self, item, spider):
        object = ArticleItem()
        object.url = item['url']
        object.headline = item['headline']
        object.content = item['content']
        object.entry = spider.unique_id
        object.save()
        return item
