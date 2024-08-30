# from template.template1 import word_template
import cfscrape
from lxml import html    

class ScraperJob:
    def __init__(self, website_url):
        self.url = website_url
        self.domain = website_url.split('/')[2]
        print(f"Hi from ScraperJob, {self.url}")

    def determine_scraper(self):
        print(self.domain)
        if self.domain == "www.merriam-webster.com":
            print(f"Scraping data from {self.domain}")
            scraper = cfscrape.create_scraper()  
            response = scraper.get(self.url).text 
            return html.fromstring(response)
            
            xpath = '//div[@class="pd-title d-flex flex-column align-items-center align-items-md-start pb-2 pb-md-0"]'
            elements = scrape_data.xpath(xpath)

            for id, element in enumerate(elements, start=1):
                word = element.xpath()