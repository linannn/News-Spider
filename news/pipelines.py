# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class NewsPipeline(object):
    def process_item(self, item, spider):
        print('---------------')
        print(item['newsTitle'])
        print(item['newsUrl'])
        print(item['newsDate'])
        print('---------------')
        return item


class NewsMySql(object):
    def process_item(self, item, spider):
        title = item['newsTitle']
        url = item['newsUrl']
        date = item['newsDate']
        source = item['newsSource']
        # text = item['newsText']

        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='spiderDB',
            charset='utf8'
        )
        cur = conn.cursor()
        print('connect to database success')
        # create table financeNewsWithoutText(id int auto_increment,source text,title text,url text,date text,primary key(id) )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        cur.execute(
            "INSERT INTO financeNewsWithoutText(source, title, url, date) values(%s, %s, %s, %s)",
            (source, title, url, date)
        )
        cur.close()
        conn.commit()
        conn.close()

        return item


class NewsMySqlWithText(object):
    def process_item(self, item, spider):
        title = item['newsTitle']
        url = item['newsUrl']
        date = item['newsDate']
        text = item['newsText']
        source = item['newsSource']

        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='spiderDB',
            charset='utf8'
        )
        cur = conn.cursor()
        print('connect to database success')
        # create table financeNews(id int auto_increment,source text,title text,url text,date text,text text,primary key(id) )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        cur.execute(
            "INSERT INTO financeNews(source, title, url, date, text) values(%s, %s, %s, %s, %s)",
            (source, title, url, date, text)
        )
        cur.close()
        conn.commit()
        conn.close()

        return item
