# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib

class ImgspiderPipeline(object):
    def process_item(self, item, spider):
        #存储图片
        for j in range(0,len(item['picurl'])):
            trueurl=item['picurl'][j]
            localpath=r"C:\Users\fan\Desktop\spider_test\pic\\"+item['picid'][j]+".jpg"
            #download
            urllib.request.urlretrieve(trueurl,filename=localpath)

        return item
