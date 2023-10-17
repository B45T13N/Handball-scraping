from pathlib import Path
from typing import Iterable, Any

import scrapy
from scrapy import Request
from scrapy.http import Response

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            #"https://quotes.toscrape.com/page/2/"
        ]

        #
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response: Response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.txt"
        file = open(filename, 'w', encoding='utf-8')

        for quote in response.xpath('//div[@class="quote"]'):
            text = quote.xpath('//span[@class="text"]/text()').extract_first()
            author = quote.xpath('//small[@class="author"]/text()').extract_first()
            tags = quote.xpath('//div[@class="tags"]/a[@class="tag"]/text()').extract()
            file.write(f"Quote : {text} \n")
            file.write(f"Author : {author}\n")
            file.write(f"Tags : {', '.join(tags)}\n")


        file.close()


