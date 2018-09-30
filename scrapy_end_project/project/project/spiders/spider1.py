# -*- coding: utf-8 -*-
import scrapy
from ..items import job58Item
from multiprocessing import Pool

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['xa.58.com']
    start_urls = ['https://xa.58.com/job/?param7503=1&from=yjz2_zhaopin&PGTID=0d202408-001e-38ed-e3d8-0b96d972df11&ClickID=1']

    def parse(self, response):

        '''
        工作分类
        '''
        link3 = response.css('.filter_items ')[0].css('li a::attr("href")')[1:].extract()
        if link3:
            for i in link3:
                link3=response.urljoin(i)

                yield scrapy.Request(url=link3, callback=self.jobs3)
    def jobs3(self,response):
        '''
        工作分类下的所有工作列表
        '''
        job_name=response.css('.name::text').extract_first()
        job_type=response.css('.crumb_item')[1].css('a::text').extract_first()#[2:]
        link4=response.css('.job_name>a::attr("href")').extract()
        if link4:
            for i in link4:
                link4=response.urljoin(i)
                yield scrapy.Request(url=link4, callback=self.detail,meta={'job_type':job_type,'job_name':job_name})
        next_=response.css('.next::attr("href")').extract_first()
        if next_:
            yield  scrapy.Request(url=next_,callback=self.jobs3)
    def detail(self,response):
        # print(response.meta,'1111111111111111111111111111111111111')
        item=job58Item()
        item['job_type']=response.meta['job_type']
        item['job_name']=response.meta['job_name']
        # try:
        #     item['job_name'] = response.css('.pos_base_info').css('span::text')[0].extract()
        # except:
        #     item['job_name']='none'
        item['job_salary'] = response.css('.pos_base_info').css('span::text')[1].extract()

        item['job_status'] =response.css('.pos_welfare span::text').extract()[0]
        #
        item['job_request_number']=response.css('.pos_base_condition span::text')[0].extract()[3:5]
        item['job_education'] =response.css('.pos_base_condition span::text')[1].extract()
        item['job_experience'] =response.css('.pos_base_condition span::text')[2].extract()
        try:
            item['job_address'] = response.css('.pos-area>span::text')[4].extract()#better choice
        except:
            item['job_address']='none'
        # item['job_address'] = response.css('.pos-area>span::text')[3].extract()
        #
        item['job_description'] ="".join(response.css('.des::text').extract())
        #
        try:
            item['company_name'] =response.css('.baseInfo_link a::text').extract()[0]
        except:
            item['company_name'] ='none'
        #item['company_attribution'] =response.css('.comp_baseInfo_belong::text').extract()[0]
        item['company_attribution']=response.css('.comp_baseInfo_belong a::text').extract()[0]
        item['company_size'] =response.css('.comp_baseInfo_scale::text').extract()[0]
        #
        # item['job_scan'] =response.css('.pos_base_statistics>span')[1].css('i::text').extract()
        # item['job_application'] =response.css('.pos_base_statistics>span')[2].css('i::text').extract()
        yield item
        #数据库：
        # 1工作分类：所有工作类型name
        # 2工作：工作名，需求人数，学历要求，经验要求，职位描述，工资，待遇，
        # 3公司：名称，类型，规模，地点，