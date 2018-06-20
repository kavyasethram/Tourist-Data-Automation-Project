from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome('C:\Users\kavya\Downloads\chromedriver_win32\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice
url = [#las vegas
       'https://www.tripadvisor.com/Hotels-g45963-oa30-Las_Vegas_Nevada-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g45963-oa60-Las_Vegas_Nevada-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g45963-oa90-Las_Vegas_Nevada-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g45963-oa120-Las_Vegas_Nevada-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g45963-oa150-Las_Vegas_Nevada-Hotels.html',
        #Los Angeles
       'https://www.tripadvisor.com/Hotels-g32655-oa30-Los_Angeles_California-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g32655-oa60-Los_Angeles_California-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g32655-oa90-Los_Angeles_California-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g32655-oa120-Los_Angeles_California-Hotels.html',
       'https://www.tripadvisor.com/Hotels-g32655-oa150-Los_Angeles_California-Hotels.html',
       #san Diego
       'https://www.tripadvisor.com/Hotels-g60750-oa30-San_Diego_California-Hotels.html#BODYCON',
       'https://www.tripadvisor.com/Hotels-g60750-oa60-San_Diego_California-Hotels.html#BODYCON',
       'https://www.tripadvisor.com/Hotels-g60750-oa90-San_Diego_California-Hotels.html#BODYCON',
       'https://www.tripadvisor.com/Hotels-g60750-oa120-San_Diego_California-Hotels.html#BODYCON'
       'https://www.tripadvisor.com/Hotels-g60750-oa150-San_Diego_California-Hotels.html#BODYCON',

       ]
url_file = open("urls_tripadvisor.txt","w+")
for i in range(len(url)):
    browser.get(url[i]) #navigate to the page
    time.sleep(10)
    html1 = browser.page_source
    html2 = browser.execute_script("return document.documentElement.innerHTML;")
    #browser.find_element_by_xpath('//a[@href="datasets/Abalone"]').click()

    ids = browser.find_elements_by_xpath('.//div[@class="prw_rup prw_meta_hsx_listing_name listing-title"]/div/a[@href]')
    #ids = set(ids)
    url_list = []
    for id in ids:
        url1 = id.get_attribute("href")
        print url1
        url_file.write(url1)
        url_file.write("\n")


url_file.close()
print len(ids)


# prices = browser.find_elements_by_xpath('.//strong[@class="item__best-price mb-gutter-half price_min"]')
# for price in prices:
#     print(price.text)
# print len(price

