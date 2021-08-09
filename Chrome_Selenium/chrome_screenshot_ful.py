
from selenium import webdriver
import chromedriver_binary
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)

url = 'https://python.org'
save_file = 'screenshot_ful.png'

def screenshot_ful(url, save_file):
  w, h = get_page_size(url)
  screenshot_size(url, save_file, w, h)

# ページの高さと幅を取得する
def get_page_size(url):
  driver = webdriver.Chrome()
  driver.get(url)
  w = driver.execute_script("return document.body.scrollWidth;")
  h = driver.execute_script("return document.body.scrollHeight;")
  driver.close()
  print('page_size=', w, h)
  return (w, h)

# 指定したサイズでページを保存
def screenshot_size(url, save_file, w, h):
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  # 画面サイズを固定
  win_size = 'window-size=' + str(w) + ',' + str(h)
  options.add_argument(win_size)
  # Chromeを起動しページを開いてスクリーンショット
  cap_driver = webdriver.Chrome(options=options)
  cap_driver.get(url)
  cap_driver.save_screenshot(save_file)
  cap_driver.close()

if __name__ == '__main__':
  screenshot_ful(url, save_file)
