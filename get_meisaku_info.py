import os, requests, csv
from bs4 import BeautifulSoup

# 画像一覧のページ
target_url ='http://uta.pw/shodou/index.php?master'
# TSVの保存パス（TSV:CSVのカンマをタブにしたもの）
save_file = 'meisaku.txt'

# HTMLを取得してBeautiful Soupで解析
html = requests.get(target_url).text
soup = BeautifulSoup(html, 'html5lib')

# CSSセレクタで.article一覧を取得
res = []
for art in soup.select('.article'):
  art_titles = art.select('.art_title')
  if len(art_titles) < 2: continue
  # 2つ目に実際の作品名と作者が入っている
  title = art_titles[1].text
  # ついでに画像URLも得る
  src = art.select('img')[0]['src']
  res.append([title, src])
  print(title, src)

# TSVをファイルに保存
with open(save_file, 'wt', encoding='utf-8') as fp:
  csv.writer(fp, delimiter='\t').writerows(res)