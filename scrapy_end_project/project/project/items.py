# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class job58Item(scrapy.Item):
    job_type=scrapy.Field()
    #工作名称和薪水
    job_name=scrapy.Field()
    job_salary=scrapy.Field()
    #工作待遇
    job_status=scrapy.Field()
    #工作需求人数，学历，经验，地址
    job_request_number=scrapy.Field()
    job_education=scrapy.Field()
    job_experience=scrapy.Field()
    job_address=scrapy.Field()
    #工作描述
    job_description=scrapy.Field()
    #公司名，类型，规模，
    company_name=scrapy.Field()
    company_attribution=scrapy.Field()
    company_size=scrapy.Field()
    #浏览，申请数量
    job_scan=scrapy.Field()
    job_application=scrapy.Field()
