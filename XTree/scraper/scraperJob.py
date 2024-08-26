import tldextract
from template.template1 import word_template

class ScraperJob:
    def __init__(self, website_url):
        self.url = website_url
        extract = tldextract.extract(self.url)
        self.domain = extract.domain
        print(f"Hi from ScraperJob, {self.website_url}")

    def determine_scraper(self):
        print(self.domain)
        if self.domain == "www.merriam-webster.com":
            print(self.domain)

