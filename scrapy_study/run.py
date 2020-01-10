# -*- coding: utf-8 -*-

from scrapy import cmdline
import os
import sys

dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dirpath)

name = '/root/PycharmProjects/scrapy_study/scrapy_study/spiders/articles.py'
cmd = 'scrapy runspider {0}'.format(name)
cmdline.execute(cmd.split())