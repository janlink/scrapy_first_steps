# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CapterraItem(scrapy.Item):
    # define the fields for your item here like:
    cat_link = scrapy.Field()
    profile_link = scrapy.Field()
# 1. Product Name
    product_name = scrapy.Field()
# 2. Who uses this software
    who_uses_software = scrapy.Field()
# 3. Category under which the service is listed
    cat_name = scrapy.Field()
# 4. Vendor name
    vendor_name = scrapy.Field()
# 5. URL
    product_url = scrapy.Field()
# 6. Country name
    country_name = scrapy.Field()
# 7. Description
    product_desc = scrapy.Field()
# 8. Feature list
    product_features = scrapy.Field()
# 9. Average rating
    avg_rating = scrapy.Field()
# 10. Number of Ratings
    review_count = scrapy.Field()
# 11. Product Details
    product_details = scrapy.Field()

