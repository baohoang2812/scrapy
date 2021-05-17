import scrapy
from scrapy import Request


class FeastSpider(scrapy.Spider):
    name = 'feast'
    allowed_domains = ['www.cgvdt.vn']
    start_urls = ['http://www.cgvdt.vn/lich-cong-giao/']

    def parse(self, response):
        # feast = response.xpath("//ul[@class='menu_center']/li/a").getall()
        data = {
            'month': '5',
            'year': '2021',
        }
        url = "http://www.cgvdt.vn/Catholic/GetList"
        # yield Request(url=url, method="POST", body='{"month": 5, "year": 2021}',
        #               headers={'X-Requested-With': 'XMLHttpRequest',
        #                        'Content-Type': 'application/json; charset=UTF-8'},
        #               callback=self.parse_data)
        # yield scrapy.FormRequest(url=url, method="POST", formdata=data, headers={'Content-Type': 'application/json'},
        #                          callback=self.parse_data)
        # yield scrapy.FormRequest(url=url, method="POST", formdata=data, headers={'Content-Type': 'text/html'},
        #                          callback=self.parse_data)
        # yield scrapy.JsonRequest(url=url, data=data, callback=self.parse_data)
        yield scrapy.FormRequest(url=url, method="POST", formdata=data,
                                 callback=self.parse_data)

    def parse_data(self, response):
        print("==========Response==========")
        # resp = response.text.encode('latin1', 'backslashreplace').decode('unicode-escape')
        feast = response.xpath('//body/p').extract()
        yield {
            'response': feast
        }
