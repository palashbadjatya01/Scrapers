from scraper.scraperJob import ScraperJob

if __name__ == '__main__':
    website_urls = [
        'https://www.merriam-webster.com/dictionary/article',
        'https://www.merriam-webster.com/dictionary/learn'
    ]
    
    for url in website_urls:
        scrape_data = ScraperJob(url)
        scrape_data.determine_scraper()