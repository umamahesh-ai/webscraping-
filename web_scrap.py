# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:00:20 2022

@author: Uma Mahesh
"""

import pandas as pd
from bs4 import BeautifulSoup as bs
import re
import requests
name = []
rating=[]
date=[]
comment=[]
pages = list(range(1,36))
for page in pages:
  req = requests.get('https://www.amazon.in/boAt-Wave-Lite-Smartwatch-Activity/product-reviews/B09V12K8NT/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}'.format(page)).text # URL of the website which you want to scrape
  #content = req.content # Get the content
  soup =bs(req,'html.parser')
  #print(soup.prettify())
  profile_name=soup.find_all('span',class_='a-profile-name')
  #print(profile_name)
  for i in range(len(profile_name)):
      name.append(profile_name[i].text)
      len(name)
  profile_rating = soup.find_all('i',class_='a-icon a-icon-star a-star-4 review-rating')
  #print(profile_rating)
 #Extracting the ratings of each person from the watch
  for i in range(len(profile_rating)):
      rating.append(profile_rating[i].text)
      len(rating)
  profile_date=soup.find_all('span',class_='a-size-base a-color-secondary review-date')
  #print(profile_date)
  for i in range(len(profile_date)):
    date.append(profile_date[i].text)
    len(date)
  profile_comment=soup.find_all('span',class_='a-size-base review-text review-text-content')
  #print(profile_comment)
  for i in range(len(profile_comment)):
      comment.append(profile_comment[i].text)
  len(comment)
  
# length of all lists
print(len(name))
print(name)
df1 = pd.DataFrame(name) 
data1=df1.rename(columns={0:'Name'})
print(len(rating))
print(rating)
df2= pd.DataFrame(rating) 
data2=df2.rename(columns={0:'Rating'})
print(len(date))
print(date)
df3 = pd.DataFrame(date)
data3=df3.rename(columns={0:'Date'})
print(len(comment))
print(comment)
df4 = pd.DataFrame(comment) 
data4=df4.rename(columns={0:'Comment'})
dataframe=pd.concat([data1,data2,data3,data4],axis=1)

dataframe.to_csv('smart_watch_webscrape.csv')















    