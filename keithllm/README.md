# How to setup development environment
Install develop tools: Visual Studio Code for coding on Windows 11 and Ubuntu 20.04
(https://code.visualstudio.com/)

Setup compiler environment: install fastapi for running on Windows and Ubuntu 20.04
(https://fastapi.tiangolo.com/tutorial/)

Local inference ollama installation: install ollama on Windows and Ubuntu 20.04 
(https://github.com/ollama/ollama)

[Ubuntu20.04]
install visual studio code on Ubuntu 20.04 (https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/)
$ sudo apt update
$ sudo apt install software-properties-common apt-transport-https wget
$ wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
$ sudo apt install code
$ sudo apt update
$ sudo apt upgrade

upgrade python version from 3.8.10 to 3.9.19
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.9
$ python3.9 --version

Get up and running with large language models locally. 
install ollama (https://github.com/ollama/ollama)
$ curl -fsSL https://ollama.com/install.sh | sh

Run ollama
$ ollama run llama3


# How to reproduce your work
You can get the up-to-date source code from git [keithksleeitri](git clone https://github.com/keithksleeitri/keithllmsrc.git)
Please change to the directory keithllmsrc
$ cd keithllmsrc
You will find this README.md file in keithllm folder.
1. Execute fast api (uvicorn main:app --port 3000)
   1. $ cd keithllmfastapi
   2. $ pip install --upgrade pip
   3. $ pip3 install openai
   4. $ pip3 install python-decouple
   5. $ pip3 install fastapi
   6. $ pip3 install click==8.0.1
   7. $ pip3 install requests
   8. $ pip3 install beautifulsoup4
   9.  Put your open ai key in .env file for protection, if you want to use chatgpt API. 
   10. $ sudo apt install uvicorn
   11. $ uvicorn main:app --port 3000

2. Open browser [llmfrontend] (http://127.0.0.1:3000/docs)
3. Execute llmchatgpt with transcription_target_url from [SayIt](https://sayit.pdis.nat.gov.tw/speeches)
   1. for example (https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿)
4. Find the result from Response body on the browser

# Anything can help other understanding your work
References:
1. Vue.js from entry to practice, ISBN 978-726-324-476-4, EL0258, 2023-06, [GOTOP](https://www.gotop.com.tw)
2. Python program design and OpenAI API applications, ISBN 978-626-333-643-8, MP22308, 2023-11 [DRMASTER](https://www.drmaster.com.tw)

# Contributer
The main contributer is Keith K.S. Lee keith.kslee@gmail.com

