# Author: Keith K.S. Lee
# Date: 2024-05-18
# Goal: obtainning url content and parsing the dialog, finally summary the dialog with chatgpt 
# To install package
# pip3 install openai
# pip3 instal python-decoupe
# pip install requests
# pip install beautifulsoup4
# put your open ai key in .env file for protection

from openai import OpenAI
from decouple import config

import requests
from bs4 import BeautifulSoup

client = OpenAI(api_key=config('OPENAI_API_KEY'))

# Try one of the following website to obtain url content
#url = 'https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿'
url = 'https://sayit.pdis.nat.gov.tw/2024-05-08-數位部例行記者會逐字稿'

# create request
html = requests.get(url)

# for debug, to show original webpage
#convert request to string datatype
#text = html.text

#print(text)

# Parsing the dialog
bs = BeautifulSoup(html.text, 'html.parser') # 解析網頁
talk_item = bs.find_all('div',{'class': 'speech__content'}) # 尋找所有標籤為div, class為'speech__content'的元素
talk_list = [] # 建立空的清單
for i in range(len(talk_item)):
    talk = talk_item[i].find('p').string
    talk_list.append(talk) # 將找到的談話新增進talk list之中
print(talk_list)

print("請稍待 ...")

# convert python list into string
my_string = ",".join(str(element) for element in talk_list)
message = "請將下面對話做總結："+ my_string

# Ask the ChatGPT to summary the dialog
completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "你會說中文, 是聰明的助理"},
  {"role": "user", "content": message}
])

# Show the finally result
response=completion.choices[0].message.content
print(response)

