from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import regex
final_list = []
browser = webdriver.Chrome('C:\Users\kavya\Downloads\chromedriver_win32\chromedriver.exe') #replace with .Firefox(), or with the browser of your choice
with open(
        "C:\\Users\\kavya\\Downloads\\chromedriver_win32\\booking\\urls_expedia.txt") as f:
    url = f.readlines()
#url = ["https://www.expedia.com/Las-Vegas-Hotels-Palace-Station-Hotel-And-Casino.h40797.Hotel-Information?chkin=4%2F23%2F2018&chkout=4%2F24%2F2018&rm1=a2&hwrqCacheKey=7ba1364a-1bf2-46d5-ae1c-009d78edaac8HWRQ1524538047312&cancellable=false&regionId=178276&vip=false&c=98825905-f261-4265-94f1-37f387d19bcb&&exp_dp=30.99&exp_ts=1524538047850&exp_curr=USD&swpToggleOn=false&exp_pg=HSR" ]
for i in range(len(url)):
    browser.get(url[i]) #navigate to the page
    #time.sleep(4)
    html1 = browser.page_source
    html2 = browser.execute_script("return document.documentElement.innerHTML;")

    ids = browser.find_elements_by_xpath(
        './/div[@class="site-content cols-row"]/header[@class="page-header"]')
    print len(ids)

    str1 =  ids[0].text
    str1 = str1.replace("\n",",")
    #sample = []

    sample = (str1.split(","))
    str2 = sample[2]
    str2 = regex.sub('[^a-zA-Z0-9-_*.]', '',str2).replace("-", "").replace(".","").strip()
    m = regex.search('\d{6}', str2)
    if m:
        z = m.start(0)
        final_list.append([sample[0],sample[1],str2[0:z],str2[z:z+11]])
    #print final_list
print len(final_list)
print final_list

with open('expedia_scrape.csv','wb') as file:
    for i in range(len(final_list)):
        file.write(str(final_list[i]))
        file.write('\n')
