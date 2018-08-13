# -*- coding: utf-8 -*-
import pymysql
class Mysql_Connect():
    conn=pymysql.connect(host='127.0.0.1',port=1234,user='root',passwd='qwe123')