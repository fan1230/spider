# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycwpjt.items import MycwpjtItem

class FanfanSpider(CrawlSpider):
    name = 'fanfan'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        #新闻网页的url
        #http://www.sohu.com/a/244757602_114731
        #allow=('http://(.*?)/a/(.*?)"')
        Rule(LinkExtractor(allow_domains=('sohu.com')), \
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = MycwpjtItem()
        i['name']=response.xpath('/html/head/title/text()').extract()
        i['link']=response.xpath('//link[@rel="canonical"]/@href').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
