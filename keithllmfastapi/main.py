import uvicorn
from fastapi import FastAPI
from openai import OpenAI
from decouple import config
from fastapi.middleware.cors import CORSMiddleware

import requests
from bs4 import BeautifulSoup

import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hichatgpt")
async def hichatgpt():
    return {"message": "Hello ChatGPT"}

@app.get("/llmsummary")
async def llmsummary():
    # Please start up ollama before call this api
    # keithkslee@keithkslee-s101A:~/keithllmsrc/keithllmfastapi$ ollama run llama3
    # Ask the llmChatGPT to summary the dialog

    # Try one of the following website to obtain url content
    url = 'https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿'
    #url = 'https://sayit.pdis.nat.gov.tw/2024-05-08-數位部例行記者會逐字稿'
    #url = 'https://sayit.pdis.nat.gov.tw/2024-05-06-總統盃黑客松第二次工作小組會議'
    #url = 'https://sayit.pdis.nat.gov.tw/2023-12-19-行政院政府資料開放諮詢小組-112-年度第-2-次會議逐字稿'

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
    message = "請將下面對話做總結並且使用繁體中文回答："+ my_string.replace("\n", "").replace(" ","")

    # Display the querry message
    print(message)

    # final data_str
    data_str = '{"model": "llama3","messages": [{ "role": "user", "content": "'+ message.replace("\n", "") + '" }], "stream": false }'

    # quick test data_str
    #data_str = '{"model": "llama3","messages": [{ "role": "user", "content": "請將下面對話做總結並且使用繁體中文回答：如何學習LLM?" }], "stream": false }'

    # Display the query string with json format
    print(data_str)

    data_str = data_str.encode('utf-8')

    completion = requests.post('http://localhost:11434/api/chat', data=data_str)

    print(f'Status Code: {completion.status_code}')
    print(f'Response Content: {completion.text}')

    if completion.status_code == 200:
      # Show the finally result
      response_data = completion.json()
      response = "The summary is " + response_data['message']['content']
      return {"summary": response.replace("\n", "")}
    else:
      return {"message": "something error"}

@app.get("/llmchatgpt/{full_path:path}")
async def llmchatgpt(full_path: str):
    # Please start up ollama before call this api
    # keithkslee@keithkslee-s101A:~/keithllmsrc/keithllmfastapi$ ollama run llama3
    # Ask the llmChatGPT to summary the dialog

    # Try one of the following website to obtain url content
    #url = 'https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿'
    #url = 'https://sayit.pdis.nat.gov.tw/2024-05-08-數位部例行記者會逐字稿'

    transcription_target_url = full_path
    
    # create request
    html = requests.get(transcription_target_url)

    # create request
    #html = requests.get(url)

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
    message = "請將下面對話做總結並且使用繁體中文回答："+ my_string.replace("\n", "").replace(" ","")

    # Display the querry message
    print(message)

    # final data_str
    data_str = '{"model": "llama3","messages": [{ "role": "user", "content": "'+ message + '" }], "stream": false }'

    # quick test data_str
    #data_str = '{"model": "llama3","messages": [{ "role": "user", "content": "請將下面對話做總結並且使用繁體中文回答：如何學習LLM?" }], "stream": false }'

    # Display the query string with json format
    print(data_str)

    data_str = data_str.encode('utf-8')

    completion = requests.post('http://localhost:11434/api/chat', data=data_str)

    print(f'Status Code: {completion.status_code}')
    print(f'Response Content: {completion.text}')

    if completion.status_code == 200:
      # Show the finally result
      response_data = completion.json()
      response = "The summary is " + response_data['message']['content']
      return {"summary": response.replace("\n", "")}
    else:
      return {"message": "something error"}

@app.get("/chatgpt/{full_path:path}")
async def chatgpt(full_path: str):
    client = OpenAI(api_key=config('OPENAI_API_KEY'))

    # Try one of the following website to obtain url content 
    #url = 'https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿'
    #url = 'https://sayit.pdis.nat.gov.tw/2024-05-08-數位部例行記者會逐字稿'
    transcription_target_url = full_path
    
    # create request
    html = requests.get(transcription_target_url)

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
    message = "請將下面對話做總結："+ my_string.replace("\n", "").replace(" ","")

    # Ask the ChatGPT to summary the dialog
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "你會說中文, 是聰明的助理"},
      {"role": "user", "content": message.replace("\n", "")}
    ])

    print(f'Response Content: {completion}')
    
    # Show the finally result
    response=completion.choices[0].message.content
    print(response)
    return {"summary": "The summary is "+response}
    

if __name__ == "__main__":
    uvicorn.run(app, port=10000)
