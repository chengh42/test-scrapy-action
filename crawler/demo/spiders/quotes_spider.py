import scrapy
from ..items import DemoItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        quote_item = DemoItem()

        for quote in response.css('div.quote'):
            quote_item["text"] = quote.css('span.text::text').get()
            quote_item["author"] = quote.css('span small::text').get()
            quote_item["tags"] = quote.css('div.tags a.tag::text').getall()

            yield quote_item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)