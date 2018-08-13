# -*- coding: utf-8 -*-
import scrapy


class Myspd1Spider(scrapy.Spider):
    name = 'myspd1'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']

    def parse(self, response):
        pass
