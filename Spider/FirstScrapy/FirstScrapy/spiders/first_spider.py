import scrapy

class DemoSpider(scrapy.spiders.Spider):
    name = 'Demo'
    start_urls = [
        'http://www.jianshu.com'
    ]
    def parse(self, response):
        print (response)