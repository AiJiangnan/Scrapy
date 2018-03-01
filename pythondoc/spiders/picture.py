# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from pythondoc.items import DocItem


class PictureSpider(scrapy.Spider):
    name = 'pythondoc'
    allowed_domains = ['usyiyi.cn']
    start_urls = ['http://python.usyiyi.cn/documents/python_352/tutorial/index.html']

    def parse(self, response):

        article_name_xpath = '/html/head/title/text()'
        article_body_xpath = '//*[@class="section"]'
        next_url_xpath = '//a[@accesskey="N"]/@href'
        next_url_prefix = 'http://python.usyiyi.cn/documents/python_352/tutorial/'

        item = DocItem()
        item['name'] = response.xpath(article_name_xpath).extract()
        item['data'] = response.xpath(article_body_xpath).extract()
        yield item
        next_url = response.xpath(next_url_xpath).extract()
        if next_url:
            next_url = next_url_prefix + next_url[0]
            yield Request(next_url)

# scrapy crawl pythondoc
