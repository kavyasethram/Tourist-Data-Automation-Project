from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome('C:\Users\kavya\Downloads\chromedriver_win32\chromedriver.exe')
url = ["https://www.expedia.com/Hotel-Search?destination=Los+Angeles%2C+CA+%28LAX-Los+Angeles+Intl.%29&latLong=33.94415%2C-118.4032&regionId=5783884&startDate=04%2F24%2F2018&endDate=04%2F25%2F2018&rooms=1&_xpid=11905%7C1&adults=1",
      "https://www.expedia.com/Hotel-Search?destination=Los+Angeles,+CA,+United+States+(LAX-Los+Angeles+Intl.)&startDate=04/24/2018&endDate=04/25/2018&adults=1&regionId=5783884&sort=recommended&page=2",
       "https://www.expedia.com/Hotel-Search?destination=Las+Vegas%2C+Nevada&latLong=36.114666%2C-115.172872&regionId=178276&startDate=04%2F24%2F2018&endDate=04%2F25%2F2018&rooms=1&_xpid=11905%7C1&adults=1",
       "https://www.expedia.com/Hotel-Search?destination=Las+Vegas+(and+vicinity),+Nevada,+United+States+of+America&startDate=04/24/2018&endDate=04/25/2018&adults=1&regionId=178276&sort=recommended&page=2",
       "https://www.expedia.com/Hotel-Search?destination=San+Diego%2C+California&latLong=32.714440%2C-117.162370&regionId=3073&startDate=04%2F24%2F2018&endDate=04%2F25%2F2018&rooms=1&_xpid=11905%7C1&adults=1",
       "https://www.expedia.com/Hotel-Search?destination=San+Diego,+California,+United+States+of+America&startDate=04/24/2018&endDate=04/25/2018&adults=1&regionId=3073&sort=recommended&page=2",]

url_file = open("urls_expedia.txt","w+")
for i in range(len(url)):
    browser.get(url[i]) #navigate to the page
    time.sleep(10)
    html1 = browser.page_source
    html2 = browser.execute_script("return document.documentElement.innerHTML;")

    ids = browser.find_elements_by_xpath('.//div[@class="flex-link-wrap"]/a[@href]')
    url_list = []
    for id in ids:
        url1 = id.get_attribute("href")
        print url1
        url_file.write(url1)
        url_file.write("\n")


url_file.close()
print len(ids)


