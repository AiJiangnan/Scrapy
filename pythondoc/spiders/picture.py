# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import time
from pythondoc.items import DocItem


class PictureSpider(scrapy.Spider):
    name = 'pythondoc'
    allowed_domains = ['readthedocs.io']
    start_urls = ['http://scrapy-chs.readthedocs.io/zh_CN/0.24/index.html']

    def __init__(self):
        self.next_url_prefix = 'http://scrapy-chs.readthedocs.io/zh_CN/0.24/'

    def parse(self, response):
        article_name_xpath = '/html/head/title/text()'
        article_body_xpath = '//div[@itemprop="articleBody"]'

        next_url_xpath = '//a[@accesskey="n"]/@href'
        _next_url_prefix = 'http://scrapy-chs.readthedocs.io/zh_CN/0.24/'

        item = DocItem()
        item['name'] = response.xpath(article_name_xpath).extract()
        item['data'] = response.xpath(article_body_xpath).extract()
        yield item
        next_url_tmp = response.xpath(next_url_xpath).extract()
        if next_url_tmp:
            next_url_tmp = str(response.xpath(next_url_xpath).extract()[0])
            next_url = self.next_url_prefix + next_url_tmp
            if next_url_tmp.find('/') > 0:
                url_list = next_url_tmp.split('/')
                if len(url_list) == 2:
                    if next_url_tmp.find('..') < 0:
                        self.next_url_prefix = _next_url_prefix + next_url_tmp.split('/')[0] + '/'
                    else:
                        self.next_url_prefix = _next_url_prefix
                elif len(url_list) == 3:
                    self.next_url_prefix = _next_url_prefix + next_url_tmp.split('/')[1] + '/'
            yield Request(next_url)

# scrapy crawl pythondoc
