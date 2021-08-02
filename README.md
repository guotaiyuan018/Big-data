# 大數據應用專題

[![hackmd-github-sync-badge](https://hackmd.io/9EHiWT-XR1mwhJxK2GcXuA/badge)](https://hackmd.io/9EHiWT-XR1mwhJxK2GcXuA)

*21728李佳謙*
###### tags: `學習歷程`
## 專題理念
希望能透過本次課程內所學知識，了解生活中大數據的應用，解決實際生活中所遇到的難題，達到學以致用的目的。同時藉此機會研究網頁相關知識，了解HTML、CSS、JavaScrip的基本概念，以及物聯網的實際應用。

## 研究原因
起初在課堂上設計了Ubike站況的爬蟲程式

![](https://i.imgur.com/asok0lQ.jpg)
```
import requests 
 
r = requests.get 
("https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json") 
 
ubikes = r.json() 
 
St1 = [ubikes['retVal']['0327']['sna'],
    ubikes['retVal']['0327']['sbi'],
    ubikes['retVal']['0327']['bemp']
    ]
St2 = [ubikes['retVal']['0169']['sna'],
    ubikes['retVal']['0169']['sbi'],
    ubikes['retVal']['0169']['bemp']
    ]
St3 = [ubikes['retVal']['0273']['sna'],
    ubikes['retVal']['0273']['sbi'],
    ubikes['retVal']['0273']['bemp']
    ]
 
 
print(St1[0],'車輛數:',St1[1],'空位數',St1[2])
print(St2[0],'車輛數:',St2[1],'空位數',St2[2])
print(St3[0],'車輛數:',St3[1],'空位數',St3[2])

```

藉由此次作業的實作中，逐漸了解爬蟲的原理與應用，並開始研究是否能藉由爬蟲與網頁內容交互，解決生活中遇到的麻煩。

## 研究初期
首先研究的是 **beautifulsoup**

beautifulsoup是一個解析HTML、XML的函式庫，可以讓開發者僅須撰寫非常少量的程式碼，就可以快速解析網頁 HTML程式碼，從中萃取出使用者有興趣的資料加以使用。

不過beautifulsoup **只能處理解析文本**，無法模仿使用者動作與網頁內容產生互動，無法滿足我希望能學以致用加以解決生活遇到難題的初衷，因此接著研究另一個工具 -- **Selenium**

Selenium 是一種應對動態網頁的爬蟲，能與網頁內容進行互動如： **點擊、滾動** 等動作，並根據撰寫腳本執行模擬用戶操作，十分適合我希望設計的專題。

## 研究目標
由於我課後經常前去國家圖書館的自修室讀書，然而座位經常是一位難求，只能一下課就趕往現場預約，或是在線上進行預約，不過線上也經常一下就一掃而空，因此產生利用網路爬蟲製作自動預約程式的想法。

在這次專題中希望能完成自動預約的**動態爬蟲系統**、並完成在Linux電腦(樹梅派)上的架設並使其定時開機運作、最後設置專屬Line Bot來通知預約詳細內容。

## 研究成果

### 程式編寫

```
#安裝selenium模組
pip install selenium
#安裝webdriver-manager
pip install webdriver_manager
#安裝requests模組
pip install requests
#安裝beautiful soup
pip install beautifulsoup4
```
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#開網頁
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sr.ncl.edu.tw/deskbook/booking/index.jsp")
```
![](https://i.imgur.com/P9eggZH.jpg)

首先匯入所需函式庫並開啟網頁

```
#點擊登入
time.sleep(1)
p1 = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[5]/td[2]/a/img')
p1.click()

#輸入帳號密碼登入
time.sleep(1)
user_id = driver.find_element_by_name('userid')
user_id.send_keys('身分證字號')
userpass = driver.find_element_by_name('userpass')
userpass.send_keys('出生年月日')
button = driver.find_element_by_id('ok')
button.click()
```
![](https://i.imgur.com/y4umgVx.png)


接著登入帳號，透過xpath、name與id尋找元素(element)，由於執行時CPU占用以及頻寬占用皆會提高，因此在執行每個步驟前皆須暫停以確保網頁已啟動完畢。

```
#選日
time.sleep(1)
tb = driver.find_element_by_id('content')
table = tb.find_element_by_xpath('.//table/tbody/tr[1]/td/table/tbody/tr[7]/td[4]/a/img')
table.click()

#選位子
time.sleep(1)
st = driver.find_element_by_id('content')
seat = st.find_element_by_xpath('.//table/tbody/tr[6]/td[2]/table/tbody/tr[4]/td[1]/img')
seat.click()
```
![](https://i.imgur.com/1bWohkb.jpg)
![](https://i.imgur.com/3jpEqlI.jpg)
再來透過id、xpath找尋自己所要預約的日期、位子
由於這邊網頁架構是使用雙層table，單單id或xpath無法精確定位元素，因此先藉由id定位包含其元素的祖先元素，再進一步使用xpath定位我們所需的日期、座位元素。

```
#利用IFTTT串聯webhook發送Line訊息
def notify ():
   url = ('https://maker.ifttt.com/trigger/reservation_success/with/key/lZnyU2O9_0ZT9vU7aa_Oaqix3XIDejhQE9QS36N0281?value1=524 ')
   r = requests.get(url) 
```
![](https://i.imgur.com/8fdemuv.png)

![](https://i.imgur.com/fZJIi2D.jpg)

IFTTT 是一個網路服務平台，可以將不同的App、連網裝置和軟體服務整合在一起，然後讓支援IFTTT 的某服務（或App、連網裝置）去觸發另一個服務（或App、連網裝置）。
目標藉由webhooks觸發，使用Line來傳送成功預約訊息，以及預約內容如：座位、時間等資訊

### 樹梅派設置
由於手上沒有適合樹梅派的小一些的螢幕，因此用SSH搭配VNC遠端操縱。
![](https://i.imgur.com/jNeju3x.png)
![](https://i.imgur.com/SZvvnvo.png)

在樹梅派上有些設置與一般linux電腦上的指令不同，這邊多加註記

```
# 安裝 Selenium 模組
pip3 install selenium
# 安裝 webdriver-manager
pip3 install webdriver-manager
```



## 遭遇問題

### given element
由於日期、座位的網頁架構皆是雙層table因此我的策略是先取得包含目標元素的祖先元素，再進一步定位。然而概念正確，執行卻屢遭挫折，中文圈的相關討論也不是太多，導致我一度想要放棄專題。直到老師建議我上Stack Overflow尋找答案，在一番查找後發現有網友的問題與我情況相似，而底下的網友答道：
> When using XPath and starting a search from a given element,you must add a '.' at the start of the locator.

```
table = tb.find_element_by_xpath('//table/tbody/tr[1]/td/table/tbody/tr[7]/td[4]/a/img')
#錯誤程式

table = tb.find_element_by_xpath('.//table/tbody/tr[1]/td/table/tbody/tr[7]/td[4]/a/img')
正確程式
```

就因為一個小小一點就導致整串程式碼無法執行，寫程式真的是一件不可馬虎的事！


---


### Covid-19
![](https://i.imgur.com/tgvRF6C.png)
由於疫情升溫以及三級警戒發布，圖書館持續休館，而自修室也隨之關閉，導致後續的測試：爬取成功預約資訊、定時自動執行皆無法測試，專題研究就此無限期暫停。

**7/27起隨北市防疫政策降級，預約系統即日隨自修室開放**

---

### 網頁結構
由於一開始對於網頁設計

## 心得感想

經過此次專題實作，除了網頁架構的相關知識了解，以及IFTTT設計操作外，還有善用外文資料來解決bug。更深刻的是學以致用的概念 -- 利用課堂中學習的知識，以及自己查找所得的資料，來解決生活中所遇到的難題，培養自己應對的能力。 


