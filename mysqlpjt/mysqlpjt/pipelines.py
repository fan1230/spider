# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class MysqlpjtPipeline(object):
    def __init__(self):
        #链接数据库
        self.conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mypydb')
    def process_item(self, item, spider):
        name=item['name'][0]
        key=item['keywd'][0]
        #构造对应的sql语句
        #conn=pymysql.connect(host='127.0.0.1',user='root',passwd='qwe123',db='spiderdb')
        #conn.query("CREATE TABLE mytb(title CHAR(20) NOT NULL,keywd CHAR(30))")
        #conn.query("INSERT INTO mytb(title,keywd) VALUES('firsttitle','firstkeywd')")


        sql="insert into mytb(title,keywd) VALUES("+name+","+key+")"
        #执行
        self.conn.query(sql)
        return item
    def close_spider(self):
        self.conn.close()
