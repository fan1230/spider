# -*- coding: utf-8 -*-
import scrapy


class Myspd3Spider(scrapy.Spider):
    name = 'myspd3'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']

    def parse(self, response):
        pass
