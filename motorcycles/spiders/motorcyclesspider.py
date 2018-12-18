# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess


class MotorcyclesspiderSpider(scrapy.Spider):
    name = 'motorcyclesspider'
    allowed_domains = ['justbikes.com.au']
    start_urls = ['http://justbikes.com.au/']
    custom_settings = {
    'LOG_FILE': 'logs/motorcycles.log',
    'LOG_LEVEL':'ERROR'
     }


    def parse(self, response):
        print('Processing...' + response.url)
