#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

# import requests
# import re
# import uuid
head={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
# def get_page(url):
#     repos=requests.get(url,headers=head)
#     return  repos
# def get_page1(url):
#     repos=requests.get(url)
#     return  repos
#
# def parse_page(page):
#      detil_urls=re.findall('<img.*src="(.*?)"',page.text,re.S)
#
#      yield detil_urls
#
# def save_pag(da):
#    with open(r'D:\tupian3\%s.jpg'%uuid.uuid4(),'wb') as f:
#        f.write(da.content)
#
# url="https://www.mzitu.com/page/{}/"
#
# for line in range(2,10):
#     url1=url.format(line)
#     #print(url1)
#     date1=get_page(url1)
#     date2=parse_page(date1)
#     for i in date2:
#         for a in i:
#             if a.endswith('com/'):
#                 continue
#             else:
#              print(a)
