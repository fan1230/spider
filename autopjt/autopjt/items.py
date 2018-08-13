# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#品名
    price=scrapy.Field()#价格
    link=scrapy.Field()#商品链接
    comnum=scrapy.Field()#评论数



