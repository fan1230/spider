# -*- coding: utf-8 -*-
import random
#导入用户池
from myfirstpjt.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.ua=ua

    def process_request(self, request, spider):
        #随机选择一个ip
        thisua=random.choice(UAPOOL)
        #输出当前user_agent
        print('当前user_agent是:'+thisua)
        #添加为具体代理
        request.headers.setdefault('User-Agent',thisua)