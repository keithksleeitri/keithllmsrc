# Noted by Keith K. S. Lee (only for keithllmfastapi)
OpenAI Key in .env, please change it to your own register key. Otherwise, you cannot to use chatgpt API.

Please start up ollama before call llmsummary or llmchatgpe api.
[Ubuntu]
Run local llm ollama: $ ollama run llama3
Run fastapi: keithllmfastapi$ uvicorn main:app --reload --host 0.0.0.0 --port 3000
[Windows] Download and Install OllamaSetup.exe
Run local llm ollama: cd C:\Users\keith\AppData\Local\Programs\
C:\Users\keith\AppData\Local\Programs>ollama run llama3
Run fastapi: keithllmfastapi> uvicorn main:app --reload --host 0.0.0.0 --port 3000
(Optional) Run frontend from keithllmsummary
C:\Keith\work\git\keithllmsrc\keithllmsummary>yarn serve
[Docker]
docker file version only use for chatgpt API only
Run fastapi: 
docker build and run on windows 11
Put your open ai key in .env file for protection, if you want to use chatgpt API.
1. C:keithllmfastapi>docker build -t keithllmfastapi .
2. C:keithllmfastapi>docker run --name keithllmbackend -p 3000:3000 keithllmfastapi
docker build on Ubuntu 22.04
Put your open ai key in .env file for protection, if you want to use chatgpt API.
1. $ cd keithllmfastapi
2. $ sudo docker build -t keithllmfastapi .
3. $ sudo docker run --name keithllmbackend -p 3000:3000 keithllmfastapi

# Try one of the following website to obtain url content
    url = 'https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿'
    url = 'https://sayit.pdis.nat.gov.tw/2024-05-08-數位部例行記者會逐字稿'
    url = 'https://sayit.pdis.nat.gov.tw/2024-05-06-總統盃黑客松第二次工作小組會議'
    url = 'https://sayit.pdis.nat.gov.tw/2023-12-19-行政院政府資料開放諮詢小組-112-年度第-2-次會議逐字稿' (This model's maximum context length is 16385 tokens. However, your messages resulted in 25631 tokens.)

# Contributer
The main contributer is Keith K.S. Lee keith.kslee@gmail.com