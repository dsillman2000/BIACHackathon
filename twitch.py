import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

site = 'https://overrustlelogs.net/Nightblue3%20chatlog/October%202018/2018-10-03'

browser=webdriver.Firefox()
browser.get(site)
soup = BeautifulSoup(browser.page_source, "html.parser")

div_box = soup.find('div', attrs={'class':'text'})
name_box = div_box.find('span')

output = name_box.get_text().encode("utf-8")


log = output.split("\n", output.count("\n"))
    

target = []

csvFile = open('twitch.csv', 'wb')
csvReader = csv.reader(csvFile)
csvWriter = csv.writer(csvFile)
for chat in log:
    if "Nightblue3" in chat or "nightblue3" in chat:
        if "streamelements" not in chat and "nightblue3:" not in chat:
            csvWriter.writerow([chat[chat.index(': ')+1:]])