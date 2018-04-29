# News-Spider
A spider based scrapy, 
使用scrapy框架,urllib库,pymsql库
运行环境ubuntu16.04 python3.5
进入news文件夹后, 在命令行输入 
> scrapy crawl newsSpider  

即可运行
- 通过更改news/settings.py文件中的ITEM_PIPELINES可以更换处理数据的方法
- NewsMySql不处理新闻文本
- NewsMySqlWithText向数据库中添加新闻文本
- financeNewsWithoutText.frm/.ibd为没有新闻文本的mysql表
- financeNews.frm/.ibd为有新闻文本的mysql表