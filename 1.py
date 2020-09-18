from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup as bs

import pandas as pd
import time

url = 'https://search.daum.net/search?w=news&sort=recency&q=%EA%B3%B5%EA%B3%B5%EC%9D%98%EB%8C%80&cluster=n&DA=PGD&dc=STC&pg=1&r=1&p=2&rc=1&at=more&sd=20200818000000&ed=20200918235959&period=u'
web = requests.get(url).content
source = bs(web,'html.parser')

for urls in source.find_all('a',{'class':'f_link_b'}):
    new_url_content = urls['href']
    print(new_url_content)
# driver = webdriver.Chrome(executable_path=r"C:/Users/Playdata/Downloads/chromedriver_win32/chromedriver.exe")
# driver.implicitly_wait(3)
# # url에 접근한다.
# driver.get('https://google.com')

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.key import Keys
# import requests
#from bs4 import BeautifulSoup as bs

# import pandas as pd
# import time
