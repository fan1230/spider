# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义结构化数据
    urlname=scrapy.Field()
    urlkey=scrapy.Field()#关键字
    urlcr=scrapy.Field()#版权信息
    urladdr=scrapy.Field()#地址
