# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from pythondoc.items import DocItem


class PictureSpider(scrapy.Spider):
    name = 'pythondoc'
    allowed_domains = ['usyiyi.cn']
    start_urls = ['http://python.usyiyi.cn/documents/python_352/tutorial/index.html']

    def parse(self, response):
        item = DocItem()
        item['name'] = response.xpath('/html/head/title/text()').extract()
        item['data'] = response.xpath('//*[@class="section"]').extract()
        yield item
        next_url = response.xpath('//a[@accesskey="N"]/@href').extract()
        if next_url:
            next_url = 'http://python.usyiyi.cn/documents/python_352/tutorial/' + next_url[0]
            yield Request(next_url)

# scrapy crawl pythondoc
