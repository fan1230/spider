# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#使用codes进行解码
import codecs
import json

class MyfirstpjtPipeline(object):
    #json格式存储
    def __init__(self):
        self.file = codecs.open(r"D:\A学习\python web\作业\18班作业\网络爬虫\测试文件\mydata2.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #通过dict(item)将item转化为一个字典
        #然后处理字典
        item1=dict(item)
        i=json.dumps(item1,ensure_ascii=False)
        line=i+'\n'
        print(line)
        # 写入文件
        self.file.write(line)
        return item
    # close_spider()在关闭蜘蛛时调用
    def close_spider(self,spider):
        self.file.close()


    # #数据结构存储
    # def __init__(self):
    #     self.file=codecs.open(r"D:\A学习\python web\作业\18班作业\网络爬虫\测试文件\mydata1.txt","wb",encoding="utf-8")
    # def process_item(self, item, spider):
    #     #设置每行写内容
    #     l=str(item)+'\n'
    #     print('haha'+l)
    #     #写入文件
    #     self.file.write(l)
    #     return item
    # #close_spider()在关闭蜘蛛时调用
    # def close_spider(self,spider):
    #     self.file.close()
