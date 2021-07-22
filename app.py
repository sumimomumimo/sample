
from bs4 import BeautifulSoup
from flask import Flask, render_template
import urllib
import urllib.parse
import urllib.request as req
import csv
import random
import pandas as pd
import numpy as np
import requests
import json
from django.shortcuts import render
import json
from collections import OrderedDict
import pprint


category = "イタリア料理"

if category == "中国料理":
    rand = 500 + random.randrange(31, 49)
    rand = str(rand)
    url = 'https://recipe.rakuten.co.jp/category/41-' + rand + '/'
if category == "韓国料理":
    rand = 550 + random.randrange(0, 18)
    rand = str(rand)
    url = 'https://recipe.rakuten.co.jp/category/42-' + rand + '/'
if category == "イタリア料理":
    rand = 500 + random.randrange(69, 82)
    rand = str(rand)
    url = "https://recipe.rakuten.co.jp/category/43-" + rand + "/"
        
#HTMLの要素を持ってくる
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#<a>タグだけをとってきたかったが、いらないやつがたくさんついてくるので、その上階層の<li>を取得
#<li>タグはたくさんあるのでfind_allを使う。仕様でfind_allで見つけたものはリストに格納される
li = soup.find_all('li',class_ = 'recipe_ranking__item')

a_tag = []

for li_tag in li:
    #<li>タグの中にある<a>は一つだけなのでfindでよい。.get('href')でhref要素を取得
    link = "https://recipe.rakuten.co.jp" + li_tag.find('a').get('href')
    a_tag.append(link)

i = random.randrange(0,len(a_tag))
print('Content-type: text/html\n')
print(a_tag[i])

d_new = {'url': str(a_tag[i])}

with open('url_box.json', 'w') as f:
    json.dump(d_new, f, indent=2, ensure_ascii=False)



