#coding:utf8
'''
Created on 2017-4-9

@author: 理工男Happy哥哥
@link: https://www.zhihu.com/people/li-gong-nan-happyge-ge/activities
'''
from os.path import os
import requests


class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
    
    def collect_data(self , data):
        if data is None:
            return
        self.datas = data
    
    def output_html(self, user_nick):
        count = 0
        
        dir_name = "image_" + user_nick
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        
        for _data in self.datas:
            
            print '正在下载第'+str(count+1)+'张图片，图片地址:'+_data['link']
            
            try:
                pic= requests.get(_data['link'], timeout=10)
            except:
                print '【错误】当前图片无法下载'
                continue
            
            string = dir_name + '/' + _data['fname']
            
            fp = open(string.decode('utf-8').encode('cp936'),'wb')
            fp.write(pic.content)
            fp.close()
        
            count += 1
            
        self.datas = []
    


