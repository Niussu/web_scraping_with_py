import scrapy

class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_request(self):
        urls = ['https://pt.wikipedia.org/wiki/Python'
                '%28progamming_language%29',
                'https://en.wikipedia.org/wiki/Functional_programming',
                'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=urls, callback=self.parse)for url in urls]
    
    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('The title is: {}'.format(title))