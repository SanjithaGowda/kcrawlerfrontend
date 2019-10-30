# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from main.models import EntryItem, ArticleItem
import json

class KcrawlerPipeline(object):
    def __init__(self, keyword, unique_id, *args, **kwargs):
        self.unique_id = unique_id

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            keyword = crawler.settings.get('keyword'),
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        if(EntryItem.objects.get(pk=self.unique_id)):
            EntryItem.objects.get(pk=self.unique_id).update(status='done')

    def process_item(self, item, spider):
        object = ArticleItem()
        #object.entry = self.unique_id
        object.content = item['content']
        object.save()
        return item
