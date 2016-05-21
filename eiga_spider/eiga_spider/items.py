# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EigaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    japan_title = scrapy.Field()
    eiga_link = scrapy.Field()
    release_date = scrapy.Field()

class MovieItem(scrapy.Item):
    original_title = scrapy.Field()
    release_date_jp = scrapy.Field()
    title_jp = scrapy.Field()
    staff = scrapy.Field()
    cast = scrapy.Field()
    movie_data = scrapy.Field()
