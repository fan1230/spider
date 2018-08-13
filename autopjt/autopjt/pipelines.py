# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
class AutopjtPipeline(object):
    def __init__(self):
        self.file=codecs.open(r"D:\A学习\python web\作业\18班作业\网络爬虫\测试文件\mydata3.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #循环遍历商品信息
        for j in range(0,len(item['name'])):
            name=item['name'][j]
            price=item['price'][j]
            link=item['link'][j]
            comnum=item['comnum'][j]
            #重新组合成字典
            goods={'name':name,'price':price,'link':link,'comnum':comnum}

            i=json.dumps(dict(goods),ensure_ascii=False)
            line=i+'\n'
            self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()
        print('运行完成!')


