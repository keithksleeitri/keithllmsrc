# To install package
# pip install requests
# pip install beautifulsoup4
 
import requests
from bs4 import BeautifulSoup
 
url = 'https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿'
 
# create request
html = requests.get(url)
 
#convert request to string datatype
#text = html.text
 
#print(text)

bs = BeautifulSoup(html.text, 'html.parser') # 解析網頁
talk_item = bs.find_all('div',{'class': 'speech__content'}) # 尋找所有標籤為div, class為'speech__content'的元素
talk_list = [] # 建立空的清單
for i in range(len(talk_item)):
    talk = talk_item[i].find('p').string
    talk_list.append(talk) # 將找到的談話新增進talk list之中
print(talk_list)
