import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = 'https://overrustlelogs.net/Riotgames%20chatlog/October%202018/2018-10-04'

browser=webdriver.Firefox()
browser.get(site)
soup = BeautifulSoup(browser.page_source, "html.parser")

div_box = soup.find('div', attrs={'class':'text'})
print(div_box)