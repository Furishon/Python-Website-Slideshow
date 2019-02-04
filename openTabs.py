from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

print('OPENING https://xkcd.com...')
driver.get('https://xkcd.com')  
time.sleep(3)
print('OPENING https://aeon.co...')
driver.get('https://aeon.co')  
time.sleep(3)
print('CLOSING...') 
driver.close()
