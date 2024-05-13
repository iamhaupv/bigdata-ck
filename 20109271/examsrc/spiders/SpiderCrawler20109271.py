import scrapy
from examsrc.items import examsrcItem

class Spider20109271(scrapy.Spider):
    name = "20109271AppCrawler"
    allowed_domains = ["books.toscrape.com"]

    fromPage = 1
    toPage = 10

    def start_requests(self):
        # Mã nguồn này đang cào dữ liệu từ trang 1 đến trang 10
        for page in range(self.fromPage,self.toPage+1):
            yield scrapy.Request(url='https://books.toscrape.com/catalogue/page-{page_num}.html'.format(page_num=page), callback=self.getBookURL20109271)

    # Lấy danh sách các URL của các quyển sách   
    def getBookURL20109271(self, response):
        bookURLs =  response.xpath('//div[@class="image_container"]//a/@href').getall()
        for bookUrl in bookURLs:
            request = scrapy.Request(url = response.urljoin(bookUrl), callback=self.getBookDetail20109271)
            yield request
    
    # Lấy thông tin từng quyển sách
    def getBookDetail20109271(self, response):
        item = examsrcItem()
        # item['title20109271'] = response.xpath('.....').get()
        # item['genre20109271'] = response.xpath('.....').get()
        # item['type20109271'] = response.xpath('.....').get()
        # item['priceex20109271'] = response.xpath('.....').get()
        # item['pricein20109271'] = response.xpath('.....').get()
        # item['tax20109271'] = response.xpath('.....').get()
        # item['ava20109271'] = response.xpath('.....').get()
        # item['review20109271'] = response.xpath('.....').get() 
        item['title20109271'] = response.xpath('//h1/text()').get()
        item['genre20109271'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        item['type20109271'] = response.xpath('//th[text()="Product Type"]/following-sibling::td/text()').get()
        item['priceex20109271'] = response.xpath('//th[text()="Price (excl. tax)"]/following-sibling::td/text()').get()
        item['pricein20109271'] = response.xpath('//th[text()="Price (incl. tax)"]/following-sibling::td/text()').get()
        item['tax20109271'] = response.xpath('//th[text()="Tax"]/following-sibling::td/text()').get()
        item['ava20109271'] = response.xpath('//th[text()="Availability"]/following-sibling::td/text()').get()
        item['review20109271'] = response.xpath('//th[text()="Number of reviews"]/following-sibling::td/text()').get() 
        yield item