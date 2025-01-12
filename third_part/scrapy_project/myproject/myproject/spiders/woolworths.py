import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import scrapy
import time

class QSpider(scrapy.Spider):
    name = 'spider_wool'

    start_urls = ['https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas']

    def start_requests(self):
        for url in self.start_urls:
            # Yield a request and include the callback function for processing the response
            yield scrapy.Request(url=url, callback=self.parse, meta={'driver': True})

    def parse(self, response):
        # Check if we are handling a response from the Selenium WebDriver
        if response.meta.get('driver'):
            # If so, use the Selenium WebDriver to load the page
            driver = self.create_driver()
            driver.get(response.url)
            
            time.sleep(30)
            page_source = driver.page_source         

            driver.quit()

            # Now we can create an HtmlResponse with the page source from Selenium
            response = scrapy.http.HtmlResponse(
                url=response.url,
                body=page_source.encode('utf-8'),
                encoding='utf-8',
            )

        # Now you can process the response as normal
        print(f"Status Code: {response.status}")
    
        breadcrumb_items = response.css('ul.breadcrumbs-linkList li a')
        breadcrumbs = [item.css('::text').get() for item in breadcrumb_items]
        print(breadcrumbs)

        yield {
            'status_code': response.status,
            'url': response.url,
            'breadcrumb': breadcrumbs
        }

    def create_driver(self):
        """Create the undetected Chrome driver."""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run headless if needed
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Initialize undetected Chrome driver
        driver = uc.Chrome(options=chrome_options)
        return driver
