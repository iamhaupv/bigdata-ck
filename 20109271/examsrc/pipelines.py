# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
import json
from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class CSVDBexamsrcPipeline:
    def process_item(self, item, spider):
        '''
        Viết code để xuất ra file csv, thông tin item trên dòng
        mỗi thông tin cách nhau với dấu ,
        Header là: nameX,genreX,typeX,priceexX,priceinX,taxX,avaX,reviewX
        Lưu dữ liệu thành file mang tên csvdataexamsrcX.csv
        '''
        with open('csvdataexamsrc20109271.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([
                item['title20109271'],
                item['genre20109271'],
                item['type20109271'],
                item['priceex20109271'],
                item['pricein20109271'],
                item['tax20109271'],
                item['ava20109271'],
                item['review20109271']
            ])
        return item
    pass
# import csv
