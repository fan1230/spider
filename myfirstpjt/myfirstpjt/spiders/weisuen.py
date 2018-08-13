# -*- coding: utf-8 -*-
import scrapy

from myfirstpjt.items import MyfirstpjtItem


class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']#允许爬行域名
    start_urls = (
        'http://blog.sina.com.cn/',
        # 'http://news.sina.com.cn/world/',
        # 'http://news.sina.com.cn',
    )
    #单个参数
    # #重写初始化方法__init__(),并设置参数myurl
    # def __init__(self,myurl=None,*args,**kwargs):
    #     super(WeisuenSpider,self).__init__(*args,**kwargs)
    #     print('要爬取的网址为:%s'%myurl)
    #     self.start_urls=['%s'%myurl]

    # #传递多个参数
    # def __init__(self,myurl=None,*args,**kwargs):
    #     super(WeisuenSpider,self).__init__(*args,**kwargs)
    #     #分割参数
    #     myurllist=myurl.split('|')
    #     for i in myurllist:
    #         print('要爬取的网址为:%s'%i)
    #         #设置起始网址列表
    #         self.start_urls=myurllist
    # # 重写start_request()
    # def start_requests(self):
    #     for i in self.start_urls:
    #         yield self.make_requests_from_url(i)

    def parse(self, response):
        item=MyfirstpjtItem()
        item['urlname']=response.xpath('/html/head/title/text()').extract()
        print('以下将显示爬取的网址的标题')
        print(item['urlname'])
        return item



#scrapy crawl weisuen -a myurl=https://www.zhaopin.com/ --nolog
#scrapy crawl weisuen -a myurl="https://www.zhaopin.com/|http://www.csdn.net" --nolog


    '''
    urls2=(
        'www.taobao.com',
        'www.jd.com',
        'www.baidu.com'
    )

    #重写start_request()
    def start_requests(self):
        for i in self.urls2:
            yield self.make_requests_from_url(i)
    '''

