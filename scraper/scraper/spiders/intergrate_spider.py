import scrapy
from scraper.items import ScraperItem


class IntergrateSpider(scrapy.Spider):
	name = "intergrate"
	start_urls = ["http://www.diemcao.vn"]

	def parse(self, response):
		# TODO: Process get element value here
		return ScraperItem(title='Test')
