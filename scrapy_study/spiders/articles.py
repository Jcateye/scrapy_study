#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.linkextractors import LinkExtractor 
from scrapy.spiders import CrawlSpider,Rule

class ArticleSpider(CrawlSpider):
    name='articles'
    
    allowed_domains = ['weibo.com']

    start_urls  = ['https://weibo.com/']

    reles = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        print('start ---------------------------')
        print(response)
        url = response.url
        title = response.css('h1').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()

        lastUpdated = lastUpdated.replace('This page wae last edited on ', '')
        print('--------------------URL is : {}'.format(url))
        print('--------------------title is : {}'.format(title))
        print('text is : {}'.format(text))
        print('Last updated : {}'.format(lastUpdated))


        