# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.selector import Selector
from news.items import NewsItem


class NewsspiderSpider(scrapy.Spider):
    name = 'newsSpider'
    allowed_domains = ['roll.finance.sina.com.cn']
    start_urls = ['http://roll.finance.sina.com.cn/finance/zq1/ywgg/index_1.shtml']

    def parse(self, response):
        spiderFlag = 0
        print('*****************************************************'+\
        '*************************************************')
        newsGroupSelector = response.xpath('//ul[@class="list_009"]')
        for sub in newsGroupSelector:
            for i in range(5):
                tempNews = NewsItem()
                newInfoSelector = sub.xpath('./li['+str(i+1)+']')
                tempNews['newsDate'] = newInfoSelector.xpath('./span/text()').extract()[0][1:-1]
                if (tempNews['newsDate'][0:2] == '02'):
                    print('------------------------------------------------')
                    print('spider finish')
                    return
                tempNews['newsTitle'] = newInfoSelector.xpath('./a/text()').extract()[0]
                tempNews['newsUrl'] = newInfoSelector.xpath('./a/@href').extract()[0]
                # 用于爬取文本
                # NewsDetail = urllib.request.urlopen(tempNews['newsUrl'])
                # NewsWebpage = NewsDetail.read().decode('utf-8')
                # newsTextSelector = Selector(text=NewsWebpage).xpath('//div[@class="article"]/p')
                # newsText = ''
                # for subText in newsTextSelector:
                #     newsText = newsText + subText.xpath('string(.)').extract()[0] + '\n'
                # tempNews['newsText'] = newsText
                yield tempNews
        # url跟进
        url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()[0]
        if url:
            page = 'http://roll.finance.sina.com.cn/finance/zq1/ywgg' + url[1:]
            yield scrapy.Request(page, callback=self.parse)
        # return news
