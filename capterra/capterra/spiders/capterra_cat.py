# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from capterra.items import CapterraItem

class CapterraCatSpider(CrawlSpider):
    name = 'capterra_cat'
    #allowed_domains = ['http://www.capterra.com/categories']
    start_urls = ['http://www.capterra.com/categories']
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        #TEMP
        for category in response.css('ol.browse-group-list'):
            if category.css('a::text').extract_first() == 'Yoga Studio':
                print 'Dong!'
                i = CapterraItem()
                i['cat_name'] = category.css('a::text').extract_first()
                i['cat_link'] = response.urljoin(category.css('a::attr(href)').extract_first())
                cat_link = i['cat_link']
                print cat_link
                request = scrapy.Request(cat_link, callback=self.parse_details)
                request.meta['item'] = i
                yield request

    def parse_details(self,response):
        print 'DETAILS!'
        item = response.meta['item']
        for detail in response.css('p.listing-description.milli'):
            item['profile_link'] = response.urljoin(detail.css('a.spotlight-link::attr(href)').extract_first())
            request = scrapy.Request(item['profile_link'], callback=self.parse_profile)
            request.meta['item'] = item
            yield request

    def parse_profile(self,response):
        print 'PROFILE'
        item = response.meta['item']
        item['product_name'] = response.css('h1.beta.no-margin-bottom::text').extract_first()
        item['who_uses_software'] = response.css('div.spotlight-target > p.epsilon > i::text').extract_first()
        item['vendor_name'] = response.css('h2.spotlight-vendor-name > span::text').extract_first()

        
        return item
            