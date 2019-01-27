# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


from time import sleep

# class BooksSpider(CrawlSpider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com/']

#     rules = (Rule(LinkExtractor(deny_domains=('google.com')),callback='parse_page',follow=False),)

#     def parse_page(self, response):
#         yield {'URL': response.url}

# class BooksSpider(Spider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']

#     def start_requests(self):
#         print('start request')
#         self.driver = webdriver.Chrome('/Users/juanjosebonilla/Desktop/Sistemas/WebProjects/ScrapyCourse/chromedriver')
#         #self.driver = webdriver.Chrome('../../chromedriver')
#         self.driver.get('http://books.toscrape.com')

#         sel = Selector(text=self.driver.page_source)
#         books = sel.xpath('//h3/a/@href').extract()
#         for book in books:
#             url = 'http://books.toscrape.com/' + book
#             yield Request(url,callback=self.parse_book)
        
#         while True:
#             try:
#                 next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
#                 sleep(3)
#                 self.logger.info('Sleeping for 3 seconds.')
#                 next_page.click()

#                 sel = Selector(text=self.driver.page_source)
#                 books = sel.xpath('//h3/a/@href').extract()
#                 for book in books:
#                     url = 'http://books.toscrape.com/catalogue/' + book
#                     yield Request(url,callback=self.parse_book)
#             except NoSuchElementException:
#                 self.logger.info('No more pages to load')
#                 self.driver.quit()
#                 break
    
#     def parse_book(self,response):
#         pass


