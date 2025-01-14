# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter

#class MakerspacescraperPipeline(object):
#    def process_item(self, item, spider):
 #       return item


class JsonPipeline(object):
    def __init__(self):
        print("in pipline init")
        self.file = open("makerspacesdata", 'w')
        print("in pipline init")
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        print("in pipline close")
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        print("in pipline process_item")
        self.exporter.export_item(item)
        return item
