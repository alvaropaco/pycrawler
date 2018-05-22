# -*- coding: utf-8 -*-
import scrapy


class ClimatempoSpider(scrapy.Spider):
    name = 'climatempo'
    allowed_domains = ['climatempo.com.br']
    start_urls = ['https://www.climatempo.com.br/climatologia/540/santos-sp/']

    def parse(self, response):
        yield {
            'cities': response.xpath('//select/option/text()').extract()
        }
