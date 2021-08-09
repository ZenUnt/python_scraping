
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()

# 作詞掲示板の作品ページを開く
url = 'https://uta.pw/sakusibbs/post.php?mml_id=35'
driver.get(url)
# class属性がposttitleの要素を取得
e = driver.find_element_by_class_name('posttitle')
# 取得したテキスト表示
print(e.text)

driver.close()