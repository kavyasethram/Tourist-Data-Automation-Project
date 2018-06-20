from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome('C:\Users\kavya\Downloads\chromedriver_win32\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice
url = ["https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNYBHIFdXNfY2GIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AED6AEB-AECkgIBeagCAw;sid=32dfd6f595a7a3e6f4c1e92bc57faec1;checkin_monthday=26&checkin_year_month=2018-04&checkout_monthday=27&checkout_year_month=2018-04&dest_id=20079110&dest_type=city&from_history=1&group_adults=2&group_children=0&no_rooms=1&si=ad&si=ai&si=ci&si=co&si=di&si=la&si=re&;sh_position=1",
       "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggJCAlhYSDNYBHIFdXNfY2GIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AEB6AEB-AECkgIBeagCAw&sid=7df7108bc301c4d8000922c9bd24eb2a&checkin_monthday=26&checkin_year_month=2018-04&checkout_monthday=27&checkout_year_month=2018-04&class_interval=1&dest_id=20079110&dest_type=city&dtdisc=0&from_history=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&sh_position=1&si=ai&si=ci&si=co&si=di&si=la&si=re&ss_all=0&ssb=empty&sshis=0&rows=15&offset=15",]
url_file = open("urls.txt","w+")
for i in range(len(url)):
    browser.get(url[i]) #navigate to the page
    time.sleep(10)
    html1 = browser.page_source
    html2 = browser.execute_script("return document.documentElement.innerHTML;")

    ids = browser.find_elements_by_xpath('.//div[@id="hotellist_inner"]/div/div/a[@href]')
    url_list = []
    for id in ids:
        url1 = id.get_attribute("href")
        print url1
        url_file.write(url1)
        url_file.write("\n")
    print len(ids)

url_file.close()



