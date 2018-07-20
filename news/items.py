from scrapy.item import Item, Field

class NewsItem(Item):
	head = Field()
	url = Field()
