# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MagnetsearchItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    magnet = scrapy.Field()
    size = scrapy.Field()
    createDate = scrapy.Field()
