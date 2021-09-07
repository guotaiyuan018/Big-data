from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#開網頁
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sr.ncl.edu.tw/deskbook/booking/index.jsp")

#點擊登入
time.sleep(1)
p1 = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[5]/td[2]/a/img')
p1.click()

#輸入登入
time.sleep(1)
user_id = driver.find_element_by_name('userid')
user_id.send_keys('F130391805')
userpass = driver.find_element_by_name('userpass')
userpass.send_keys('20040111')
button = driver.find_element_by_id('ok')
button.click()

#選日
time.sleep(1)
tb = driver.find_element_by_id('content')
table = tb.find_element_by_xpath('.//table/tbody/tr[1]/td/table/tbody/tr[7]/td[4]/a/img')
table.click()

#選位子
time.sleep(1)
st = driver.find_element_by_id('content')
seat = st.find_element_by_xpath('.//table/tbody/tr[6]/td[2]/table/tbody/tr[1]/td[1]/a/img')
seat.click()

#獲取預約成功資訊
soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find('div',id = 'printablediv')				
name = table.find('img',title = '讀者姓名').parent.next_sibling.next_sibling.string
date = table.find('img',title = '預約日期').parent.next_sibling.next_sibling.string



#設置ifttt觸發
def notify ():
    
   url = ('https://maker.ifttt.com/trigger/reservation_success/with/key/lZnyU2O9_0ZT9vU7aa_Oaqix3XIDejhQE9QS36N0281?value1=524 ')
   r = requests.get(url)
   
notify()
'''
