#coding:utf8
'''
Created on 2017-4-9

@author: 理工男Happy哥哥
@link: https://www.zhihu.com/people/li-gong-nan-happyge-ge/activities
'''
from tuchong import url_manager, html_parser, html_outputer, html_downloader


class SpiderMain(object):
    
    def __init__(self):
        self.urls       = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser     = html_parser.HtmlParser()
        self.outputer   = html_outputer.HtmlOutputer()
        
    def craw(self, root_url, user_nick):
        
        html_cont = self.downloader.download(root_url)
        new_urls = self.parser.parse_albums_urls(root_url, user_nick, html_cont)
        
        count = 1
        for link in new_urls:
            
            self.urls.add_new_url(link)
            while self.urls.has_new_url():
                try:
                    new_url = self.urls.get_new_url()
                    html_cont = self.downloader.download(new_url)
                    print "craw %d : %s"%(count , new_url)
                    new_data = self.parser.parse_image(new_url,html_cont)
                    # self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)
                    
                    count = count + 1
                except:
                    print "craw fail"
            
            self.outputer.output_html(user_nick)


if __name__ == "__main__":
    
    print "begin"
    
    user_nick = "shaineyy"
    root_url = "https://tuchong.com/424887/albums/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, user_nick)
    
    print "finish"
