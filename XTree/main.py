from scraper.scraperJob import ScraperJob

if __name__ == '__main__':
    website_url = ['https://www.merriam-webster.com/dictionary/article'
                   , 'https://www.merriam-webster.com/dictionary/learn'
                ]
    for url in website_url:
        ScraperJob(url)