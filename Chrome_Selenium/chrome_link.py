
from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()

# 作詞掲示板のトップページを開く
driver.get('https://uta.pw/sakusibbs/')

# 名作アーカイブというリンクを探す
link = driver.find_element_by_link_text('名作アーカイブ')
# 見つけたリンクをクリック
link.click()

time.sleep(30)
driver.close()