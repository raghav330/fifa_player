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

        def extract_with_xpath(query, extract_all=False):
            if extract_all:
                return response.xpath(query).extract_all()
            return response.xpath(query).extract_first().strip()

        yield {
            'id': extract_with_css("div.info h1::text"),
            'full_name': extract_with_css("div.meta::text"),
            'positions': extract_with_css("div.meta span::text", getall=True),
            'b_h_w': extract_with_css("div.meta::text", getall=True)[-1],
            'overall_rating': extract_with_xpath("//div[@class='column col-4 text-center'][1]/span/text()"),
            'potential': extract_with_xpath("//div[@class='column col-4 text-center'][2]/span/text()"),
            'value': extract_with_xpath("//div[@class='column col-4 text-center'][3]/span/text()"),
            'wage': extract_with_xpath("//div[@class='column col-4 text-center'][4]/span/text()"),
            'preferred_foot': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[1]/text()[2]"),
            'international_reputation': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[2]/text()[2]"),
            'weak_foot': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[3]/text()[2]"),
            'skill_moves': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[4]/text()[2]"),
            'work_rate': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[5]/span/text()"),
            'body_type': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[6]/span/text()"),
            'release_clause': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[8]/span/text()"),
            'club_team': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[1]/a/text()"),
            'club_team': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[1]/a/text()"),
            'club_rating': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[2]/span/text()"),
            'club_position': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[3]/span/text()"),
            'club_jersey_number': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[4]/text()"),
            'club_join_date': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[5]/text()[2]"),
            'national_team': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[1]/a/text()"),
            'national_rating': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[2]/span/text()"),
            'national_team_position': extract_with_path("//div[@class='teams']/div[1]/div[4]/ul/li[3]/span/text()"),
            'national_jersey_number': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[4]/text()"),

        }
