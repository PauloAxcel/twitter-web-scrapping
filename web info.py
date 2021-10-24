# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 12:04:00 2021

@author: PAULO ALEXANDRE DE CARVALHO GOMES
"""
import requests
import sys
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer


url_0 = 'https://www.linguistweets.org/2020/programa/h/'

url_changes = ['0','3','6','9','12','15','16','21']

dataset = []

for u in url_changes:
    url = url_0+u
    
    response = requests.get(url)
    
    body = response.text
    
    tree = html.fromstring(body)
    
    titles = tree.xpath('//a[@class="program__item-title-link"]/text()')
    #change the 'a' before the @, into the class prefix
    abstracts = tree.xpath('//div[@class="program__item-excerpt text"]/text()')
    #print("\n".join(extracteditems))
    #link = tree.xpath('//h1[@class="program__item-title title-02"]/text()')
    
    
    
    soup = BeautifulSoup(body)
    
    links = []
    
    for link in soup.find_all('a'):
        for l in link.get('href').split('/'):
            if l == 'status':
                links.append(link.get('href'))
                
    f_links = list(set(links))
    
    
    dataset.append([[u]*len(titles),titles,abstracts,f_links])


import pandas as pd
import numpy as np

df = pd.DataFrame()
for d in dataset:
    df = df.append(pd.DataFrame(d).T)
    

df.columns = ['iteration','title','abstract','link']

df.to_csv('Abstracts.csv',index=None)




