# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class examsrcItem(scrapy.Item):
    title20109271 = scrapy.Field() # Title
    genre20109271 = scrapy.Field() # Genre
    type20109271 = scrapy.Field() # Type
    priceex20109271 = scrapy.Field() # Price exclude tax
    pricein20109271 = scrapy.Field() # Price include tax
    tax20109271 = scrapy.Field() # Tax
    ava20109271 = scrapy.Field() # Availability
    review20109271 = scrapy.Field() # Number of reviews
