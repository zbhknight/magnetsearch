# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from magnetsearch.items import MagnetsearchItem

class MagnetSpider(scrapy.Spider):
    name = "magnet"
    allowed_domains = ["www.torrentkitty.tv"]
    start_urls = []

    def start_requests(self):
        _keywoard = raw_input('Input Keyword:')
        yield self.make_requests_from_url('https://%s/search/%s/' %
                (self.allowed_domains[0], _keywoard))

    def parse(self, response):
        if response.body.strip() == "":
            return
        sel = Selector(response)
        if '/search/' in response.url:
            _hrefs = sel.xpath('//a[@rel="information"]/@href').extract()
            for _uri in _hrefs:
                yield(Request("https://%s/%s" % (self.allowed_domains[0], _uri)))
        else:
            _name = sel.xpath('//h2')[0].xpath('text()').extract()[0]
            _magenet = sel.xpath('//textarea[@class="magnet-link"]/text()').extract()[0]
            _table = sel.xpath('//table[@class="detailSummary"]')
            _tds = _table.xpath('.//td')
            _date = _tds[3].xpath('text()').extract()[0]
            _size = _tds[4].xpath('text()').extract()[0]
            yield MagnetsearchItem(name=_name, magnet=_magenet, createDate=_date, size=_size)
