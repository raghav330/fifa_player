# -*- coding: utf-8 -*-
import scrapy


class FifaSpider(scrapy.Spider):
    name = 'fifa_spider'

    start_urls = ['https://sofifa.com/players/']

    def parse(self, response):
        for href in response.xpath("//tbody/tr/td[2]/div/a[2]/@href"):
            yield response.follow(href, self.parse_player)

        for href in response.xpath("//a[@class='btn pjax']/@href"):
            yield response.follow(href, self.parse)

    def parse_player(self, response):

        def extract_with_css(query, getall=False):
            if getall:
                return response.css(query).getall()
            return response.css(query).get(default='').strip()

        yield {
            'id': extract_with_css("div.info h1::text"),
            'full_name': extract_with_css("div.meta::text"),
            'positions': extract_with_css("div.meta span::text", getall=True),
        }
