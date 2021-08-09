
from selenium import webdriver
import chromedriver_binary
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)

# Googleのトップページを開く
driver.get('https://uta.pw/sakusibbs/users.php?user_id=1')

# CSSセレクターで作品一覧を取得
a_list = driver.find_elements_by_css_selector('ul#mmlist li a')
# 一覧を反復表示
for a in a_list:
  print('■', a.text) # 作品名
  print('└', a.get_attribute('href')) # URL

driver.close()