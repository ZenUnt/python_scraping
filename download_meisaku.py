import os, time, requests, urllib
from bs4 import BeautifulSoup

# 画像一覧のページ
target_url ='http://uta.pw/shodou/index.php?master'
# 保存先フォルダ
save_dir = './image-meisaku'

def download_images():
  # 名作一覧のページHTMLを取得
  html = requests.get(target_url).text
  # 解析して画像URLの一覧を取得
  urls = get_image_urls(html)
  # URLの一覧をダウンロード
  go_download(urls)

# HTMLから画像のURL一覧を取得
def get_image_urls(html):
  soup = BeautifulSoup(html, 'html5lib')
  # 画像URLを取得
  res = []
  for img in soup.find_all('img'):
    src = img['src']
    # URLを絶対パスに変換
    url = urllib.parse.urljoin(target_url, src)
    print('img.src=', url)
    res.append(url)
  return res

# 連続でURL一覧をダウンロード
def go_download(urls):
  if not os.path.exists(save_dir):
    os.mkdir(save_dir)
  # 連続でダウンロード
  for url in urls:
    # ローカルファイル名決定
    fname = os.path.basename(url)
    save_file = save_dir + '/' + fname
    # ダウンロード 
    r = requests.get(url)
    with open(save_file, 'wb') as fp:
      fp.write(r.content)
      print("save:", save_file)
    time.sleep(1)

if __name__ == '__main__':
  download_images()
  

