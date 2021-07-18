from bs4 import BeautifulSoup

with open('fish.html', encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# CSSセレクタでウナギの値段を探す
p = soup.select('div#eel > p.price')
print(p[0].string)
