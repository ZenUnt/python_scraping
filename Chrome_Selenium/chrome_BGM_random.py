
from selenium import webdriver
import chromedriver_binary
import os, time, random

login_url = 'https://play.generative.fm/browse'
driver = webdriver.Chrome()

def play_bgm(driver):
  driver.get(login_url)
  time.sleep(2)
  a = driver.find_elements_by_class_name('_1t7QTVnS8YYY0hrg2BRak_')
  ran = random.randint(0, len(a)) - 1
  a[ran].click()
  b = driver.find_elements_by_class_name('MuiSvgIcon-root')
  b[2].click()

if __name__ == '__main__':
  play_bgm(driver)
