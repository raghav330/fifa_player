# -*- coding: utf-8 -*-
import scrapy


class FifaSpider(scrapy.Spider):
    name = 'fifa_spider'

    start_urls = ['https://sofifa.com/players/']

    def parse(self, response):
        for href in response.xpath("//tbody/tr/td[2]/div/a[2]/@href"):
            yield response.follow(href, self.parse_player)

        for href in response.xpath("//a[@class='btn pjax']/@href"):
            if href is not None:
                yield response.follow(href, self.parse)

    def parse_player(self, response):

        def extract_with_css(query, getall=False):
            if getall:
                return response.css(query).getall()
            return response.css(query).get(default='').strip()

        def extract_with_xpath(query, extract_all=False):
            if extract_all:
                return response.xpath(query).extract()
            return response.xpath(query).extract_first(default='').strip()

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
            'international_reputation(1-5)': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[2]/text()[2]"),
            'weak_foot(1-5)': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[3]/text()[2]"),
            'skill_moves(1-5)': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[4]/text()[2]"),
            'work_rate': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[5]/span/text()"),
            'body_type': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[6]/span/text()"),
            'release_clause': extract_with_xpath("//div[@class='teams']/div[1]/div[1]/ul/li[8]/span/text()"),

            'club_team': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[1]/a/text()"),
            'club_team': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[1]/a/text()"),
            'club_rating': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[2]/span/text()"),
            'club_position': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[3]/span/text()"),
            'club_jersey_number': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[4]/text()"),
            'club_join_date': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[5]/text()[2]"),
            'contract_end_year': extract_with_xpath("//div[@class='teams']/div[1]/div[3]/ul/li[6]/text()[2]"),

            'national_team': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[1]/a/text()"),
            'national_rating': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[2]/span/text()"),
            'national_team_position': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[3]/span/text()"),
            'national_jersey_number': extract_with_xpath("//div[@class='teams']/div[1]/div[4]/ul/li[4]/text()"),

            'crossing': extract_with_xpath("//div[@class='mt-2 mb-2']/div[1]//ul/li[1]/span[1]/text()"),
            'finishing': extract_with_xpath("//div[@class='mt-2 mb-2']/div[1]//ul/li[2]/span[1]/text()"),
            'heading_accuracy': extract_with_xpath("//div[@class='mt-2 mb-2']/div[1]//ul/li[3]/span[1]/text()"),
            'short_passing': extract_with_xpath("//div[@class='mt-2 mb-2']/div[1]//ul/li[4]/span[1]/text()"),
            'volleys': extract_with_xpath("//div[@class='mt-2 mb-2']/div[1]//ul/li[5]/span[1]/text()"),

            'dribbling': extract_with_xpath("//div[@class='mt-2 mb-2']/div[2]//ul/li[1]/span[1]/text()"),
            'curve': extract_with_xpath("//div[@class='mt-2 mb-2']/div[2]//ul/li[2]/span[1]/text()"),
            'freekick_accuracy': extract_with_xpath("//div[@class='mt-2 mb-2']/div[2]//ul/li[3]/span[1]/text()"),
            'long_passing': extract_with_xpath("//div[@class='mt-2 mb-2']/div[2]//ul/li[4]/span[1]/text()"),
            'ball_control': extract_with_xpath("//div[@class='mt-2 mb-2']/div[2]//ul/li[5]/span[1]/text()"),

            'acceleration': extract_with_xpath("//div[@class='mt-2 mb-2']/div[3]//ul/li[1]/span[1]/text()"),
            'sprint_speed': extract_with_xpath("//div[@class='mt-2 mb-2']/div[3]//ul/li[2]/span[1]/text()"),
            'agility': extract_with_xpath("//div[@class='mt-2 mb-2']/div[3]//ul/li[3]/span[1]/text()"),
            'reactions': extract_with_xpath("//div[@class='mt-2 mb-2']/div[3]//ul/li[4]/span[1]/text()"),
            'balance': extract_with_xpath("//div[@class='mt-2 mb-2']/div[3]//ul/li[5]/span[1]/text()"),

            'shot_power': extract_with_xpath("//div[@class='mt-2 mb-2']/div[4]//ul/li[1]/span[1]/text()"),
            'jumping': extract_with_xpath("//div[@class='mt-2 mb-2']/div[4]//ul/li[2]/span[1]/text()"),
            'stamina': extract_with_xpath("//div[@class='mt-2 mb-2']/div[4]//ul/li[3]/span[1]/text()"),
            'strength': extract_with_xpath("//div[@class='mt-2 mb-2']/div[4]//ul/li[4]/span[1]/text()"),
            'long_shots': extract_with_xpath("//div[@class='mt-2 mb-2']/div[4]//ul/li[5]/span[1]/text()"),

            'aggression': extract_with_xpath("//div[@class='mb-2'][2]/div[1]//ul/li[1]/span[1]/text()"),
            'interceptions': extract_with_xpath("//div[@class='mb-2'][2]/div[1]//ul/li[2]/span[1]/text()"),
            'positioning': extract_with_xpath("//div[@class='mb-2'][2]/div[1]//ul/li[3]/span[1]/text()"),
            'vision': extract_with_xpath("//div[@class='mb-2'][2]/div[1]//ul/li[4]/span[1]/text()"),
            'penalties': extract_with_xpath("//div[@class='mb-2'][2]/div[1]//ul/li[5]/span[1]/text()"),
            'composure': extract_with_xpath("//div[@class='mb-2'][2]/div[1]//ul/li[6]/span[1]/text()"),

            'marking': extract_with_xpath("//div[@class='mb-2'][2]/div[2]//ul/li[1]/span[1]/text()"),
            'standing_tackle': extract_with_xpath("//div[@class='mb-2'][2]/div[2]//ul/li[2]/span[1]/text()"),
            'sliding_tackle': extract_with_xpath("//div[@class='mb-2'][2]/div[2]//ul/li[3]/span[1]/text()"),

            'GK_diving': extract_with_xpath("//div[@class='mb-2'][2]/div[3]//ul/li[1]/span[1]/text()"),
            'GK_handling': extract_with_xpath("//div[@class='mb-2'][2]/div[3]//ul/li[2]/span[1]/text()"),
            'GK_kicking': extract_with_xpath("//div[@class='mb-2'][2]/div[3]//ul/li[3]/span[1]/text()"),
            'GK_positioning': extract_with_xpath("//div[@class='mb-2'][2]/div[3]//ul/li[4]/span[1]/text()"),
            'GK_reflexes': extract_with_xpath("//div[@class='mb-2'][2]/div[3]//ul/li[5]/span[1]/text()"),

            'tags': extract_with_xpath("//div[@class='teams']/div[2]/a/text()", extract_all=True),

            'LS': extract_with_xpath("//div[@class='columns mb-2'][1]/div[2]/text()[2]"),
            'ST': extract_with_xpath("//div[@class='columns mb-2'][1]/div[3]/text()[2]"),
            'RS': extract_with_xpath("//div[@class='columns mb-2'][1]/div[4]/text()[2]"),
            'LW': extract_with_xpath("//div[@class='columns mb-2'][2]/div[1]/text()[2]"),
            'LF': extract_with_xpath("//div[@class='columns mb-2'][2]/div[2]/text()[2]"),
            'CF': extract_with_xpath("//div[@class='columns mb-2'][2]/div[3]/text()[2]"),
            'RF': extract_with_xpath("//div[@class='columns mb-2'][2]/div[4]/text()[2]"),
            'RW': extract_with_xpath("//div[@class='columns mb-2'][2]/div[5]/text()[2]"),

            'LAM': extract_with_xpath("//div[@class='columns mb-2'][3]/div[2]/text()[2]"),
            'CAM': extract_with_xpath("//div[@class='columns mb-2'][3]/div[3]/text()[2]"),
            'RAM': extract_with_xpath("//div[@class='columns mb-2'][3]/div[4]/text()[2]"),

            'LM': extract_with_xpath("//div[@class='columns mb-2'][4]/div[1]/text()[2]"),
            'LCM': extract_with_xpath("//div[@class='columns mb-2'][4]/div[2]/text()[2]"),
            'CM': extract_with_xpath("//div[@class='columns mb-2'][4]/div[3]/text()[2]"),
            'RCM': extract_with_xpath("//div[@class='columns mb-2'][4]/div[4]/text()[2]"),
            'RM': extract_with_xpath("//div[@class='columns mb-2'][4]/div[5]/text()[2]"),

            'LWB': extract_with_xpath("//div[@class='columns mb-2'][5]/div[1]/text()[2]"),
            'LDM': extract_with_xpath("//div[@class='columns mb-2'][5]/div[2]/text()[2]"),
            'CDM': extract_with_xpath("//div[@class='columns mb-2'][5]/div[3]/text()[2]"),
            'RDM': extract_with_xpath("//div[@class='columns mb-2'][5]/div[4]/text()[2]"),
            'RWB': extract_with_xpath("//div[@class='columns mb-2'][5]/div[5]/text()[2]"),

            'LB': extract_with_xpath("///div[@class='card-body']/div[@class='columns']/div[1]/text()[2]"),
            'LCB': extract_with_xpath("//div[@class='card-body']/div[@class='columns']/div[2]/text()[2]"),
            'CB': extract_with_xpath("//div[@class='card-body']/div[@class='columns']/div[3]/text()[2]"),
            'RCB': extract_with_xpath("//div[@class='card-body']/div[@class='columns']/div[4]/text()[2]"),
            'RB': extract_with_xpath("//div[@class='card-body']/div[@class='columns']/div[5]/text()[2]"),
        }
