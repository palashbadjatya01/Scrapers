import cfscrape
from lxml import html    
class word_template:
    def __init__(self, xpath_trace):
        self.url = xpath_trace

    # Function to scrape the webpage using cfscrape
    def scrape(self):
        scraper = cfscrape.create_scraper()  
        response = scraper.get(self.url).text 
        return html.fromstring(response)
    
    xpath = '//div[@class="pd-title d-flex flex-column align-items-center align-items-md-start pb-2 pb-md-0"]'
    elements = scrape_data.xpath(xpath)

    for id, element in enumerate(elements, start=1):
        word = element.xpath()