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
user_id.send_keys('帳號')
userpass = driver.find_element_by_name('userpass')
userpass.send_keys('密碼')
button = driver.find_element_by_id('ok')
button.click()

#選日
time.sleep(1)
tb = driver.find_element_by_id('content')
table = tb.find_element_by_xpath('.//table/tbody/tr[1]/td/table/tbody/tr[1]/td[4]/a/img')
table.click()

#選位子
time.sleep(1)
st = driver.find_element_by_id('content')
seat = st.find_element_by_xpath('.//table/tbody/tr[6]/td[6]/table/tbody/tr[1]/td[1]/a/img')
seat.click()

#獲取預約資訊
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
inf = []
td_tags = soup.find_all('td')
for tag in td_tags:
      inf.append(tag.string)
      
ink={ "value1" :inf[5].strip() , "value2" : inf[11].strip() + inf[13].strip(), "value3" : inf[15].strip() }
name = inf[5].strip()
time = inf[11].strip() + inf[13].strip()
seat = inf[15].strip()

#設置ifttt觸發
url = ('https://maker.ifttt.com/trigger/reservation_success/with/key/lZnyU2O9_0ZT9vU7aa_Oaqix3XIDejhQE9QS36N0281?value1='+name+'&value2='+time+'&value3='+seat )
r = requests.post(url)
