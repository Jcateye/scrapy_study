#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class demo(scrapy.Spider):
    name = 'demo'

    allowed_domians = ['weibo.com']
    start_urls = [
        "https://weibo.com/a/hot/aea1fc45409a8500_0.html?type=grap",
        "https://weibo.com/a/hot/7cbcd5e5c0ce0d55_0.html?type=grab"
    ]

    def parse(self, response):
        filename =response.url.split('/')[-2]
        with open(filename,'wb') as f:
            f.write(response.body)