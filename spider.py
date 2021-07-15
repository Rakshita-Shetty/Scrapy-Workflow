import scrapy
from ..items import BooksItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'`
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/',
                  'http://books.toscrape.com/catalogue/page-2.html',
                  'http://books.toscrape.com/catalogue/page-3.html']
    
    def parse(self, response):
        items = BooksItem()
        all_books = response.xpath('//article[@class="product_pod"]')
        
        for book in all_books:
            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div/p[@class="price_color"]/text()').extract_first()
            image_url = self.start_urls[0] + book.xpath('.//img[@class="thumbnail"]/@src').extract_first()
            book_url = self.start_urls[0] + book.xpath('.//h3/a/@href').extract_first()
            yield {
                'title': title,
                'price': price,
                'Image URL': image_url,
                'Book URL': book_url,
                }