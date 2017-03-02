# coding: utf-8
import scrapy
from datetime import datetime


class NatureSpider(scrapy.Spider):
    name = "nature"

    def start_requests(self):
        url = 'http://www.nature.com/nature/archive/category.html?code=archive_orig_research'
        year_month_str = getattr(self, 'ym', None)
        if year_month_str is not None:
            try:
                year_month = datetime.strptime(year_month_str, '%Y%m')
                url += '&{:year=%Y&month=%m}'.format(year_month)
            except:
                pass
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # crawl all articles in the current page
        for article in response.css('article'):
            article_type = article.css('h1 span::text').extract_first()
            if article_type != 'Article':
                continue
            article_url = response.urljoin(
                article.css('h1 a::attr(href)').extract_first())
            yield scrapy.Request(article_url, callback=self.parse_article)

        # find link to the next page
        next_page_url = response.css(
            '.list-header ul.paging li.next a::attr(href)').extract_first()
        if next_page_url:
            # crawl the next page
            yield scrapy.Request(
                url=response.urljoin(next_page_url), callback=self.parse)

    def parse_article(self, response):
        url = response.url
        title = response.css(
            'h1.article-heading::text').extract_first().strip()
        abstract = response.css('div#abstract p::text').extract_first().strip()
        yield dict(url=url, title=title, abstract=abstract)
