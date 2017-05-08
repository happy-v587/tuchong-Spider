#coding:utf8
'''
Created on 2017-4-9

@author: 理工男Happy哥哥
@link: https://www.zhihu.com/people/li-gong-nan-happyge-ge/activities
'''
from bs4 import BeautifulSoup
import json


class HtmlParser(object):
    
    def _get_albums_urls(self, page_url, user_nick, soup):        
        new_urls = set()
        links = soup.find_all('a' , class_="albums")
        print links
        for link in links:
            new_url = link['href']
            album_id = new_url[-7:-1]
            new_full_url = "https://" + user_nick + ".tuchong.com/rest/2/albums/" + album_id + "/images"
            new_urls.add(new_full_url)
            print new_full_url
        
        return new_urls
    
    def parse_albums_urls(self,page_url, user_nick, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont , 'html.parser' , from_encoding='utf-8')
        new_urls = self._get_albums_urls(page_url, user_nick, soup)
        
        return new_urls
        
    def _get_new_data(self, page_url, datas):        
        
        res_data = []
        for img in datas['data']['image_list']:
            print str(img['img_id']) + ".jpg"
            data = {}
            data['link'] = "https://photo.tuchong.com/" + str(img['user_id']) + "/f/" + str(img['img_id']) + ".jpg"
            data['fname'] = str(img['img_id']) + ".jpg"
            res_data.append(data)
        
        return res_data
    
    def parse_image(self,page_url,html_cont):
        
        if page_url is None or html_cont is None:
            return
        
        res =  json.loads(html_cont)
        
        new_data = self._get_new_data(page_url , res)
        
        return new_data
