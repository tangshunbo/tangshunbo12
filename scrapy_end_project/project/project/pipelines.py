# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import job58Item
from pymongo import MongoClient
import pymysql
class ProjectPipeline(object):
    def process_item(self, item, spider):
        return item
#========================================================================================
class job58Pipeline(object):
    def open_spider(self,spider):
        self.__conn = pymysql.connect(host='127.0.0.1', port=3306, db='tang2', user='root', password='root',
                                      charset='utf8') #连接pymysql
        self.cu = self.__conn.cursor(pymysql.cursors.DictCursor)#转换成字典
    def process_item(self, item, spider):
        if isinstance(item, job58Item):
            # 查询分类id
            sql = 'select id from job_type where type_name=%s'
            flag = self.cu.execute(sql, (item['job_type'],))#执行sql语句，将获取的分类传入sql查询中
            if flag:
                type_id = self.cu.fetchone()['id']###查询id
            else:
                sql = 'insert into job_type (type_name) values(%s)'
                self.cu.execute(sql, (item['job_type'],))
                self.__conn.commit()###提交数据必须代码
                type_id = self.cu.lastrowid###获取插入数据的自增id
                # print(type_id,'00000000000000000000000000')
            # 查询工作id
            sql = 'select id from job_msg where job_name=%s and job_salary=%s and job_request_number=%s and job_description=%s'#只用工作名称
            flag = self.cu.execute(sql, (item['job_name'],item['job_salary'],item['job_request_number'],item['job_description']))
            if flag:
                job_id = self.cu.fetchone()['id']
                # print(job_id,'+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            else:
                sql = 'insert into job_msg (job_name,job_salary,job_status,job_request_number,job_education,job_experience,job_description,type_id)values(%s,%s,%s,%s,%s,%s,%s,%s)'
                self.cu.execute(sql, (item['job_name'], item['job_salary'], item['job_status'],item['job_request_number'], item['job_education'], item['job_experience'],item['job_description'], type_id))
                self.__conn.commit()
                job_id = self.cu.lastrowid
                # print(job_id,'--------------------------------------------------------')
            # 存入内容
            sql = "select * from company_msg where company_name=%s and job_id=%s"
            flag = self.cu.execute(sql, (job_id, item['company_name']))
            if flag == 0:
                sql = 'insert into company_msg (company_name,company_attribution,company_size,job_address,job_id) values (%s,%s,%s,%s,%s)'
                self.cu.execute(sql, (item['company_name'], item['company_attribution'], item['company_size'],item['job_address'],job_id))
                self.__conn.commit()
        return item
    def close_spider(self, spider):
        self.cu.close()
        self.__conn.close()
#===================================================================================
class job58_testPipeline(object):
    def open_spider(self,spider):
        self.m=MongoClient()#连接数据库
        self.db=self.m.job58#进入数据库
        self.col=self.db[spider.name]#获取数据集
    def process_item(self, item, spider):
        if isinstance(item, job58Item):
           self.col.insert_one(dict(item))
            # 将item返回以待后继的pipeline进行处理
        return item
    def close_spider(self,spider):
        self.m.close()