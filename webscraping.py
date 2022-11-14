# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:07:18 2022

@author: Uma Mahesh
"""

# import libraries 

from bs4 import BeautifulSoup as bs
import requests
import re

name=soup.find_all('span',class_='a-profile-name')
content=soup.find_all('a',class_='review-title-content')
rating=soup.find_all('i',class_='review-rating')
comment =soup.find_all('span',class_='review-text-content')
date =soup.find_all('span',class_='review-date')

watch_review=[]
for i in range(1,35):
    ip=[]
url='https://www.amazon.in/Fire-Boltt-Borderless-Display-Swimming-Tracking/product-reviews/B0B8Z5RC4X/ref=cm_cr_getr_d_paging_btm_next_4?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
response= requests.get(url)
soup=bs(response.content,'html.parser')
name=soup.find_all('span',class_='a-profile-name')
content=soup.find_all('a',class_='review-title-content')
rating=soup.find_all('i',class_='review-rating')
comment =soup.find_all('span',class_='review-text-content')
date =soup.find_all('span',class_='review-date')
reviews=[name,content,rating,comment,date]
for i in reviews:
    print(i[6])
    #ip.append(reviews[i].text)
watch_review=watch_review+ip












