# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from heise.items import HeiseItem


class HeiseStartSpider(CrawlSpider):
    name = 'heise_start'
    # allowed_domains = ['https://www.heise.de']
    start_urls = ['https://www.heise.de']

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # my_container = list()
        for news_item in response.css('div.indexlist_item'):
            article_page = news_item.css('section header h3 a::attr(href)').extract_first()
            article_page = response.urljoin(article_page)
            # yield {
            #     'title': news_item.css('section header h3 a::attr(title)').extract_first(),
            #     'date': news_item.css('section ul.indexlist_info li.date::text').extract_first()
            # }
            item = HeiseItem()
            item['title'] = news_item.css('section header h3 a::attr(title)').extract_first()
            item['date'] = news_item.css('section ul.indexlist_info li.date::text').extract_first()
            request = scrapy.Request(article_page, callback=self.parse_author)
            request.meta['item'] = item
            yield request


        next_page = response.css('a.seite_weiter::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
 

    def parse_author(self, response):
        item = response.meta['item']
        item['author'] = response.css('span.author::text').extract_first()
        item['time'] = response.css('time::text').extract_first()
        return item

    # def parse_time(self, response):
    #     item = response.meta['item']
    #     item['time'] = response.css('time::text').extract_first()
    #     return item
            