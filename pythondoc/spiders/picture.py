# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import time
from pythondoc.items import DocItem


class PictureSpider(scrapy.Spider):
    name = 'pythondoc'
    allowed_domains = ['readthedocs.io']
    start_urls = ['http://scrapy-chs.readthedocs.io/zh_CN/0.24/index.html']
    next_urls = []

    def parse(self, response):

        article_name_xpath = '/html/head/title/text()'
        article_body_xpath = '//div[@itemprop="articleBody"]'
        next_url_xpath = '//div[@class="wy-menu wy-menu-vertical"]//a//@href'
        next_url_prefix = 'http://scrapy-chs.readthedocs.io/zh_CN/0.24/'

        item = DocItem()
        item['name'] = response.xpath(article_name_xpath).extract()
        # item['data'] = response.xpath(article_body_xpath).extract()
        item['data'] = response.xpath(next_url_xpath).extract()
        yield item
        next_urls = response.xpath(next_url_xpath).extract()
        for url in next_urls:
            next_url = next_url_prefix + url
            yield Request(next_url, callback=self.parse_subpage)

    def parse_subpage(self, response):
        article_name_xpath = '/html/head/title/text()'
        article_body_xpath = '//div[@itemprop="articleBody"]'
        item = DocItem()
        item['name'] = response.xpath(article_name_xpath).extract()
        # item['data'] = response.xpath(article_body_xpath).extract()
        return item

# scrapy crawl pythondoc
