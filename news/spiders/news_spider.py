from scrapy import Spider
from scrapy.selector import Selector

from news.items import NewsItem
from news.spiders.src import topic

class NewsSpider(Spider):
	#subscribe = Topic()
	my_url = "https://www.ndtv.com/topic/"
	#strng = subscribe.topic()
	content = topic().replace(" ","-")
	name = 'news'
	allowed_domains = ["https://www.ndtv.com"]
	start_urls = [my_url + content
	]

	def parse(self, response):
		title = response.css(".header.fbld strong::text").extract()
		link =  response.css(".header.fbld a::attr(href)").extract()

		for item in zip(title,link):
			scraped_info = {			
			'title' : item[0],
			'link' : item[1],
			}
			yield scraped_info