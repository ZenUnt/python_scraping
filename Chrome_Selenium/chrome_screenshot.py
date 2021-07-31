
from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()
driver.get('https://python.org')
driver.save_screenshot('screenshot.png')
driver.quit()