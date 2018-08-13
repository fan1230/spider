# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from scrapy.http import Request
from hexunpjt.items import HexunpjtItem

class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    #设置要爬取的用户uid,方便博主赋值
    uid='fjrs168'
    #使用start_requests方法编写首次爬取行为
    def start_requests(self):
        #模拟成浏览器
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html",headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64;x64,rv:61.0) Gecko/20100101 Firefox/61.0'
        })

    def parse(self, response):
        item=HexunpjtItem()
        item['name']=response.xpath('//span[@class="ArticleTitleText"]/a/text()').extract()
        item['url']=response.xpath('//span[@class="ArticleTitleText"]/a/@href').extract()

        #需用正则匹配
        pat_hits='click(.*?)<'
        pat_comment='comment(.*?)<'
        filter_first1=re.compile(pat_hits).findall(str(response.body))
        filter_first2=re.compile(pat_comment).findall(str(response.body))
        pat_hits='>(\d*?)<'
        pat_comment='>(\d*?)<'
        item['hits']=re.compile(pat_hits).findall(str(filter_first1))
        item['comment']=re.compile(pat_comment).findall(str(filter_first2))

        yield item

        #获取总页数
        pat='blog.hexun.com/p(\d*?)/'
        data=re.compile(pat).findall(str(response.body))#--->list
        # if (len(data)>=2):
        #     totalurl=data[-2]
        # totalurl=1
        # print('一共'+str(totalurl)+'页')

        for i in range(2,10):
            #构造下次要爬的url
            nexturl="http://"+str(self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
            yield Request(nexturl,callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64;x64,rv:61.0) Gecko/20100101 Firefox/61.0'
            })


