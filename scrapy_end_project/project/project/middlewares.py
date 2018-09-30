# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import random
from time import sleep
class ProjectSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProjectDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        headers_msg={
            'referer': 'https: // webim.58.com / index?p = rb',
            'cookie': 'userid360_xml=101106D2A2D635EA94EA0AC11B271EF0; time_create=1539916058767; commontopbar_new_city_info=483%7C%E8%A5%BF%E5%AE%89%7Cxa; f=n; id58=Ze072VuY2K2vZ1m7rfNWzg==; 58tj_uuid=9b187808-9d63-44c9-adaf-8066d05b9c11; als=0; xxzl_deviceid=MxHbHzhoUnA%2FG6S1VQ7Zbh5WhS0eu%2FWuz78gbPAo2OH0bHpzWpkIbz%2BMTzlYX04s; wmda_uuid=3e594f9bb13dfe4388ee1b32384c8735; wmda_new_uuid=1; gr_user_id=190579aa-d8dc-40a4-a815-6086993ddb54; show_zcm_banner=true; wmda_visited_projects=%3B2385390625025%3B6333604277682%3B1731916484865%3B1731918550401%3B1732038237441; param8616=0; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1537266138; isSmartSortTipShowed=true; param8716kop=0; 58home=xa; bProtectShowed=true; mcity=xa; city=xa; commontopbar_new_city_info=483%7C%E8%A5%BF%E5%AE%89%7Cxa; commontopbar_ipcity=xa%7C%E8%A5%BF%E5%AE%89%7C0; __utma=253535702.601656450.1537328144.1537362829.1537408013.3; __utmz=253535702.1537408013.3.3.utmcsr=xa.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/job/; f=n; sessionid=ba5a1492-e39a-4210-8dcf-cfb14781ea92; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1537408819,1537408940,1537416686,1537416920; wmda_session_id_1731916484865=1537419996088-1bba4f37-e889-415b; new_uv=13; utm_source=; spm=; init_refer=https%253A%252F%252Fcallback.58.com%252Ffirewall%252Fvalid%252F1971860171.do%253Fnamespace%253Dinfodetailweb%2526url%253Dhttps%25253A%25252F%25252Fxa.58.com%25252Fyewu%25252F34316614248393x.shtml%25253Fadtype%25253D1%252526finalCp%25253D000001230000000000000000000000000000_104390804201512310070187148%252526adact%25253D3%252526psid%25253D104390804201512310070187148%252526iuType%25253Dq_2%252526ClickID%25253D3%252526ytdzwdetaildj%25253D0%252526entinfo%25253D34316614248393_q%252526PGTID%25253D0d302408-001e-3da8-5f59-bd67a0a063ec; new_session=0; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1537423684,1537423717,1537423785,1537423801; JSESSIONID=636853B9777AD89FFE29F1A268212300; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1537424100; gr_session_id_b4113ecf7096b7d6=38b613da-9dda-4e66-b6c8-ae20b15d63a1; gr_session_id_b4113ecf7096b7d6_38b613da-9dda-4e66-b6c8-ae20b15d63a1=true; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1537425741; ppStore_fingerprint=C2E969A4DD97464876FA24277170B7414B4018738B60E298%EF%BC%BF1537425741862',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        request.headers.update(headers_msg)
        # 代理
        # proxy_list=[
        #     "http://124.172.117.189:80",
        #     "http://219.133.31.120:8888",
        #     "http://183.237.194.145:8080",
        #     "http://183.62.172.50:9999",
        #     "http://163.125.157.243:8888",
        #     "http://183.57.42.79:81",
        #     "http://202.103.150.70:8088",
        #     "http://182.254.129.124:80",
        #     "http://58.251.132.181:8888",
        #     "http://112.95.241.76:80"
        # ]
        # proxy_url=random.choice(proxy_list)
        # request.meta['proxy'] = proxy_url
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
