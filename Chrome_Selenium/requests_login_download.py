import os, time, requests, urllib
from bs4 import BeautifulSoup

login_url = 'https://uta.pw/sakusibbs/users.php?' + \
            'action=login&m=try'
user_id, password = ('JS-TESTER', 'ipCU12ySxI')
save_file = './list2.csv'

def login_download():
  # Requestsでセッションを開始
  session = requests.Session()
  # ログインフォームを送信
  res = session.post(login_url, params={
    'username_mmlbbs6': user_id,
    'password_mmlbbs6': password})
  time.sleep(1)
  # ログイン後のページからマイページを得る
  mypage_url = get_link(res.text, 'マイページ')
  mypage_html = session.get(mypage_url).text
  time.sleep(1)
  # マイページからCSVのダウンロードURLを得る
  csv_url = get_link(mypage_html, 'CSVでダウンロード')
  # ダウンロードして保存
  download_save(session, csv_url)

# HTMLを解析してリンクURLを取得
def get_link(html, label):
  soup = BeautifulSoup(html, 'html5lib')
  # a要素を全部調べてラベルに一致するURLを返す
  for a in soup.find_all('a'):
    if label in a.text:
      url = urllib.parse.urljoin(login_url, a['href'])
      print('url=', url)
      return url
  # 見つからなかった場合
  print(label + 'が見当たりません')
  quit()

# CSVをダウンロード
def download_save(session, csv_url):
  res = session.get(csv_url)
  with open(save_file, "wt") as fp:
    fp.write(res.text)
    print(res.text)

if __name__ == '__main__':
  login_download()
