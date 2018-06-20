from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome('C:\Users\kavya\Downloads\chromedriver_win32\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice
url = ["https://www.tripadvisor.com/Hotels-g45963-Las_Vegas_Nevada-Hotels.html",]
       #"https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggJCAlhYSDNYBHIFdXNfY2GIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AEB6AEB-AECkgIBeagCAw&sid=7df7108bc301c4d8000922c9bd24eb2a&checkin_monthday=26&checkin_year_month=2018-04&checkout_monthday=27&checkout_year_month=2018-04&class_interval=1&dest_id=20079110&dest_type=city&dtdisc=0&from_history=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&sh_position=1&si=ai&si=ci&si=co&si=di&si=la&si=re&ss_all=0&ssb=empty&sshis=0&rows=15&offset=15",]
url_file = open("urls1.txt","w+")
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

