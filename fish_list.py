from bs4 import BeautifulSoup

with open('fish.html', encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# CSSセレクタで魚の一覧を得る
res = []
div_list = soup.select('#fishes > div')
for div in div_list:
  # divの子要素にあるh2を得る
  fish = div.h2.text
  # さらにCSSセレクタで検索
  desc = div.select('.desc')[0].text
  price = div.select('.price')[0].text
  print(fish, desc, price)
  # 結果をリストに格納
  res.append([fish, desc, price])

# CSVに変換して非保存
import csv
with open('fish.csv', 'wt', encoding="utf-8") as fp:
  csv.writer(fp).writerows(res)
