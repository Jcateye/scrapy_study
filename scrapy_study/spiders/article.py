#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        urls=['https://baike.baidu.com/item/java/85979',
              'https://baike.baidu.com/item/c%E8%AF%AD%E8%A8%80',
              'https://baike.baidu.com/item/Python/407313']
        return [ scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_fist()
        print('URL IS {}'.format(url))
        print('Title IS {}'.format(title))
