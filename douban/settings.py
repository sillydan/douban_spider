# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban'
#设置爬取的第一页小组
#GROUP_URL='https://www.douban.com/group/G4/discussion?start=0'
#我每天每夜的自拍 小组
GROUP_URL='https://www.douban.com/group/duqi/discussion?start=0'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

#设置下载超时时间
DOWNLOAD_TIMEOUT = 300

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

#设置延迟时间,单位为s,豆瓣每分钟超过40次请求就会403
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept-Encoding': 'br, gzip, deflate',
#    'Cookie':'__utma=30149280.1493325172.1535859396.1535879509.1535883623.6; __utmb=30149280.14.5.1535884095994; __utmc=30149280; __utmv=30149280.14480; __utmz=30149280.1535859396.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_doumail_num=0; push_noty_num=0; _pk_id.100001.8cb4=1cbd1a16281bf1e5.1535859395.6.1535884096.1535881759.; _pk_ses.100001.8cb4=*; __utmt=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1535883623%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2iO42UpgpVLJ3lPopuxXFbckM3SIHfAJWhEXSwUSewP98jrTz3s7vkbaE4ITf_sQ%26wd%3D%26eqid%3D8ba62e430000b51d000000035b8b5abd%22%5D; ck=ciNZ; dbcl2="144804313:EIVI5AOKs1w"; ps=y; as="https://sec.douban.com/b?r=https%3A%2F%2Fwww.douban.com%2Fgroup%2FG4%2Fdiscussion%3Fstart%3D0"; ll="108296"; ap_v=1,6.0; douban-fav-remind=1; __yadk_uid=fkAy6WFuJXtMOpWaZM9Of17zlIy3gOcq; bid=7uit5jyIy8Q',
#    'Host':'www.dou ban.com',
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Connection': 'keep-alive',
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
#    'Accept-Language': 'zh-cn',}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban.middlewares.DoubanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'douban.middlewares.DoubanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'douban.pipelines.DoubanPipeline': 300,
}
IMAGES_STORE = './pic'


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
