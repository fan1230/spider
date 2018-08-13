# -*- coding: utf-8 -*-
#middlewares下载中间件
#导入随机函数,目的是随机挑选一个ip
import random
#导入ip池
from myfirstpjt.settings import IPPOOL
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip=ip
        #请求处理
    def process_request(self, request, spider):
        #随机选择一个ip
        thisip=random.choice(IPPOOL)
        #输出当前ip
        print('当前ip是:'+thisip['ipaddr'])
        #添加为具体代理
        request.meta['proxy']='http://'+thisip['ipaddr']