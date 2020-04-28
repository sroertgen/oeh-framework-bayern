import scrapy

base_url = 'https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/'
start_urls = []

for i in range(1, 14):
    start_urls.append(base_url + i + '/englisch'

class FrameworkSpider(scrapy.spider):
    name="framework_bavaria"

    def parse(self, response):
        fullStatement
        humanCodingScheme
        smartLevel
