# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb


class DailiIpsPipeline(object):
    # 该函数必须返回一个具有数据的dict或者item对象
    def process_item(self, item, spider):
        con = MySQLdb.connect('127.0.0.1', 'root', 'mysql', 'test', charset="utf8", use_unicode=True)
        # 下面这行代码表示设置MySQL使用的字符集为utf8
        con.set_character_set('utf8')
        cur = con.cursor()
        insert_sql = "insert into proxy (ip, port, position, type, speed, last_check_time)values ('%s', '%s', '%s', '%s', '%s', '%s')" % (item['ip'], item['port'], item['position'], item['type'], item['speed'], item['last_check_time'])
        # 插入数据库
        cur.execute(insert_sql)
        con.commit()
        con.close()
