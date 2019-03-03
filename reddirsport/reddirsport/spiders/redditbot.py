# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['https://www.reddit.com/r/sports/']
    start_urls = ['http://https://www.reddit.com/r/sports//']

    def parse(self, response):
        pass
