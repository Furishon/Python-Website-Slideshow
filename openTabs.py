from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

def openUrl(url, onTime):
	'''OPENS A SPECIFIED URL AND KEEPS IT OPEN FOR (ATLEAST) A SPECIFIED AMOUNT OF TIME
ARGS:
	url: string, THE EXACT URL TO OPEN,
	onTime: int, THE NUMBER OF SECONDS TO KEEP URL OPEN'''
	print('OPENING {}'.format(url))
	driver.get(url)
	time.sleep(onTime) 

f = open('urls.txt', 'r')
urlList = f.readlines()
for url in urlList:
	openUrl(url=str(url), onTime=3)	

print('CLOSING...') 
driver.close()
