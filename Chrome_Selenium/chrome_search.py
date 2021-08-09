
from selenium import webdriver
import chromedriver_binary
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)

# Googleのトップページを開く
driver.get('https://google.com')

# 検索ボックスを探す
el = driver.find_element_by_name('q')
# キーワードを入力
el.send_keys('Pythonの教科書')
# フォームを送信する
el.submit()

time.sleep(10)
driver.close()