# -*- coding: utf-8 -*-
import scrapy
from imgspider.items import ImgspiderItem
import re
from scrapy.http import Request

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = ['http://www.58pic.com/piccate/3-0-0.html']

    def parse(self, response):
        item=ImgspiderItem()
        pat1="(http://pic.qiantucdn.com/58pic/.*?.jpg)"#原图 compile 编译括号里的代码
        item['picurl']=re.compile(pat1).findall(str(response.body))
        #构建图片名称
        pat2="http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item['picid']=re.compile(pat2).findall(str(response.body))
        yield item
        #遍历列表页
        for i in range(1,2):
            nexturl='http://www.58pic.com/piccate/3-0-0-default-0_2_0_0_default_0-'+str(i)+'.html'
            yield Request(nexturl,callback=self.parse,)
