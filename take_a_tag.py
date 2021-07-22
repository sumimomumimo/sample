import requests
from bs4 import BeautifulSoup

#5,6行目でHTMLの要素を持ってくる
response = requests.get('https://recipe.rakuten.co.jp/category/41-531/')
soup = BeautifulSoup(response.text, 'lxml')

#<a>タグだけをとってきたかったが、いらないやつがたくさんついてくるので、その上階層の<li>を取得
#<li>タグはたくさんあるのでfind_allを使う。仕様でfind_allで見つけたものはリストに格納される
li = soup.find_all('li',class_ = 'recipe_ranking__item')

a_tag = []

for li_tag in li:
    #<li>タグの中にある<a>は一つだけなのでfindでよい。.get('href')でhref要素を取得
    link = "https://recipe.rakuten.co.jp" + li_tag.find('a').get('href')
    a_tag.append(link)

print(a_tag[7])