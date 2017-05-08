#coding:utf8
'''
Created on 2017-4-9

@author: 理工男Happy哥哥
@link: https://www.zhihu.com/people/li-gong-nan-happyge-ge/activities
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url, timeout=10)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
