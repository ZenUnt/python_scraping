import requests, urllib, os, time
from bs4 import BeautifulSoup

save_dir = './pydoc_tutorial'
top_page = 'https://docs.python.org/ja/3/tutorial/index.html'
check_url = 'https://docs.python.org/ja/3/tutorial/'
# すでに訪問済みのページ
visited = {}

# 指定されたURLのページを取得する
def get_page(url):
  # 取得対象か調べる
  if check_url not in url: return
  # すでに巡回済みか調べる
  if url in visited: return
  visited[url] = True # 訪問済みにする
  # ダウンロード
  res = requests.get(url)
  # 文字コードが正しく設定されない場合に設定
  res.encoding = res.apparent_encoding
  html = res.text
  # HTMLを保存
  fname = save_dir + '/' + os.path.basename(url)
  if not os.path.exists(save_dir):
    os.mkdir(save_dir) # フォルダがなければ作成
  with open(fname, 'wt', encoding="utf-8") as f:
    f.write(html)
    print('save:', fname)
  time.sleep(1)
  # Beautiful Soupで解析
  soup = BeautifulSoup(html, 'html5lib')
  for a in soup.find_all('a'):
    # 絶対URLに変換
    a_url = urllib.parse.urljoin(url, a['href'])
    # URLのフラグメントを削除
    a_url = urllib.parse.urldefrag(a_url)[0]
    # ページを取得
    get_page(a_url)

if __name__== '__main__':
  get_page(top_page) # トップページを取得
