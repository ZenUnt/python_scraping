
from selenium import webdriver
import chromedriver_binary
import os, time

login_url = 'https://uta.pw/sakusibbs/users.php?action=login'
user_id, password = ('JS-TESTER', 'ipCU12ySxI')
save_dir = os.path.dirname(os.path.abspath(__file__))
save_file = save_dir + '/list.csv'
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', { 'download.default_directory': save_dir})
driver = webdriver.Chrome(options = options)

def login_download():
  driver = webdriver.Chrome(options=options)
  try_login(driver)
  link_click(driver, 'マイページ')
  link_click(driver, 'CSVでダウンロード')
  for i in range(30):
    if os.path.exists(save_file): break
    time.sleep(1)
  driver.close()

def try_login(driver):
  driver.get(login_url)
  usr = driver.find_element_by_name('username_mmlbbs6')
  usr.send_keys(user_id)
  pwd = driver.find_element_by_name('password_mmlbbs6')
  pwd.send_keys(password)
  pwd.submit()

def link_click(driver, label):
  a = driver.find_element_by_partial_link_text(label)
  a.click()

if __name__ == '__main__':
  login_download()
