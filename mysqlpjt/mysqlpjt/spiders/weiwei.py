# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mysqlpjt.items import MysqlpjtItem

class WeiweiSpider(CrawlSpider):
    name = 'weiwei'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    # http: // news.sina.com.cn / w / 2018 - 08 - 02 / doc - ihhehtqf6321726.shtml
    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'),\
                           allow_domains=('sina.com.cn')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MysqlpjtItem()
        i['name']=response.xpath('/html/head/title/text()').extract()
        if response.xpath('//meta[@name="keywords"]/@content').extract()==[]:
            i['keywd'] = response.xpath('//div[@id="keywords"]/@data-wbkey').extract()
        i['keywd']=response.xpath('//meta[@name="keywords"]/@content').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
