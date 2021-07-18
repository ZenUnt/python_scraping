from bs4 import BeautifulSoup

with open('fish.html', encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# h2の一覧を得る
for h2 in soup.find_all('h2'):
  if h2.string == 'ウナギ':
    # 兄弟要素を調べる
    for e in h2.next_siblings:
      # p要素を調べる
      if e.name == 'p':
        if e['class'][0] == 'price':
          print(e.string)
