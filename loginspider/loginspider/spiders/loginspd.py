# -*- coding: utf-8 -*-
import scrapy,urllib
from scrapy.http import Request,FormRequest

class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    #模拟成浏览器
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64;x64,rv:61.0) Gecko/20100101 Firefox/61.0"
    }

    def start_requests(self):
        #第一次进入,回调
        return [
            Request('https://www.douban.com/accounts/login',meta={'cookiejar':1},
                    callback=self.parse)
        ]

    def parse(self, response):
        #判断有无验证码
        captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()
        if len(captcha)>0:
            print('此时有验证码呦')
            locapath=r"C:\Users\fan\Desktop\spider_test\captcha\JKL.png"
            #存储到本地
            urllib.request.urlretrieve(captcha[0],filename=locapath)
            print('请查看本地图片,并输入对应的验证码:')
            captcha_value=input()
            #设置要传递的post信息
            data={
                #账号
                'form_email':'1163997392@qq.com',
                'form_password':'qwe123465',
                'captcha-solution':captcha_value,
                #转向个人中心
                'redir':'https://www.douban.com/people/182332610/'
            }
        else:
            print('此时没有验证码')
            data={
                'form_email': '1163997392@qq.com',
                'form_password': 'qwe123465',
                'redir': 'https://www.douban.com/people/182332610/'
            }
        print('登录中...')
        #通过FormRequest.from_response()登录
        return [
            FormRequest.from_response(
                response,
                # meta={'cookiejar':response.maea['cookiejar']},
                # headers=self.header,
                formdata=data,
                callback=self.next
            )
        ]
    def next(self,response):
        print('此时已经完成登录,提取用户相关信息')
        xtitle='/html/head/title/text()'
        xnotetitle='//div[@class="note-header pl2"]/a/@title'
        xnotetime='//div[@class="note-header pl2"]//span[@class="pl"]/text()'
        xnotecontent='//div[@class="note-header pl2"]/div[@class="note"]/text()'
        xnoteurl='//div[@class="note-header pl2"]/a/@href'

        title=response.xpath(xtitle).extract()
        notetitle=response.xpath(xnotetitle).extract()
        notetime=response.xpath(xnotetime).extract()
        notecontent=response.xpath(xnotecontent).extract()
        noteurl=response.xpath(xnoteurl).extract()
        print('网页的标题是:'+title[0])
        for i in range(0,len(notetitle)):
            print('第'+str(i+1)+'篇文章的信息如下')
            print('文章的标题为:'+notetitle[i])
            print('发表时间为:'+notetime[i])
            print('内容为:'+notecontent[i])
            print('链接:'+noteurl[i])
            print('-----------------------')
