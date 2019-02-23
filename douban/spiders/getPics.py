import scrapy
from douban.items import DoubanItem
import requests
import os
from douban.settings import IMAGES_STORE,GROUP_URL


class Pics(scrapy.Spider):
    name='getPic'
    cookie = {
        'Cookie': '__utma=30149280.1493325172.1535859396.1535876818.1535879509.5; __utmb=30149280.47.2.1535880000349; __utmc=30149280; __utmz=30149280.1535859396.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=1,6.0; douban-fav-remind=1; bid=7uit5jyIy8Q'}
    def start_requests(self):
        #定义爬取的链接
        urls=[GROUP_URL]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parseUrl)
            # 爬取到的页面如何处理？提交给parse方法处理

    def parseUrl(self, response):
        #定义爬取规则
        #获取帖子url
        urls=response.css('.olt tr .title a::attr(href)').extract()
        #auther=response.css('.olt tr td[nowrap] a[href]::text').extract()
        #result=list(zip(title,url,auther))
        #self.log(result)
        #with open (filename,'wb') as f:
        #    f.write(result)
        #self.log('保存文件：%s'%filename)

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parsePic)
        next_url=response.css('.paginator .next link::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parseUrl)

    def parsePic(self,response):
        #获取帖子首页楼主正文的图片
        header = {
            'USER-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15', }
        dir_path = '{}'.format(IMAGES_STORE)
        auther=response.css('.topic-doc .from a::text').extract_first()
        urls=response.css('.topic-doc img::attr(src)').extract()
        dir = '{}//{}'.format(dir_path, auther)
        if (not os.path.exists(dir)) and urls:
            os.makedirs(dir)
        for url in urls:
            pic_name=auther+url.split('/')[-1]
            with open('{}//{}'.format(dir,pic_name), 'wb') as f:
                req = requests.get(url, headers=header)
                f.write(req.content)
                self.log('保存文件：%s' % pic_name)




