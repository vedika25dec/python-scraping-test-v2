import scrapy
from scrapy_splash import SplashRequest


#version : scrapy 2.8.0  , scrapy-splash - 0.9.0 , Twisted==21.2.0 , six

class QSpider(scrapy.Spider):
    name = 'spider_edeka'

    start_urls = ['https://www.edeka24.de/Lebensmittel/Suess-Salzig/Schokoriegel/']  # URL to start scraping from

    def start_requests(self):
        for url in self.start_urls:
         
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # Print the status code of the response
        print(f"Status Code: {response.status}")

        breadcrumb_items = response.css('div.breadcrumb li a')

        # Create a list of breadcrumb items with both the text and the href link
        breadcrumbs = []
        for item in breadcrumb_items:
            breadcrumbs.append(item.css('::text').get())


        # Extract specific items like product names and prices if needed (example using CSS selectors)
        product_list = response.css('ul#jqList li') 
        
        # Yield the result with status code, URL, raw HTML content, and scraped product names

        for product in product_list:
            product_name = product.css('div.product-details a.title h2::text').get()

            yield {
                'status_code': response.status,
                'url': response.url,
                'breadcrumb':breadcrumbs,
                'product_name': product_name  # List of product titles
                
            }

