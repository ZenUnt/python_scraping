from bs4 import BeautifulSoup

# HTMLファイルを読み込む
with open('fish.html', encoding='utf-8') as fp:
  html_str = fp.read()

# BeautifulSoupオブジェクト作成
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示
title = soup.find('title')
print(title.text)