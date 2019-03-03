# -*- coding: utf-8 -*-
import scrapy


class BukalapakSpider(scrapy.Spider):
    name = 'bukalapak'
    allowed_domains = ['https://www.bukalapak.com/c/komputer/laptop']
    start_urls = ['https://www.bukalapak.com/c/komputer/laptop/']

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        product_name=response.css(".product__name::text").extract()
        #Extract data using xpath
        price_range=response.xpath("//div[@class='product-price']/span/span[@class='amount positive']/text()").extract()
        cicilan=response.xpath("//div[@class='product-installment if-bbm-this-should-be-hidden']/span/text()").extract()

        row_data=zip(product_name,price_range,cicilan)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'product_name' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'price_range' : item[1],
                'cicilan' : item[2]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

