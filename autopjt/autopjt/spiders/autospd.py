# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4011029.html']
    print('启动中...')

    def parse(self, response):

        item=AutopjtItem()
        item['name']=response.xpath('//a[@class="pic"]/@title').extract()
        item['price']=response.xpath('//span[@class="price_n"]/text()').extract()
        item['link']=response.xpath('//a[@class="pic"]/@href').extract()
        item['comnum']=response.xpath('//a[@name="itemlist-review"]/text()').extract()
        yield item

        for i in range(1,20):
            url='http://category.dangdang.com/pg'+str(i)+'-cid4011029.html'
            #指定爬取网址和回调函数 实现自动爬取
            yield Request(url,callback=self.parse)

