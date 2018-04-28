# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    newsTitle = scrapy.Field()
    newsUrl = scrapy.Field()
    newsDate = scrapy.Field()
    newsText = scrapy.Field()
