# -*- coding: utf-8 -*-
import scrapy


class Myspd2Spider(scrapy.Spider):
    name = 'myspd2'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']

    def parse(self, response):
        pass
