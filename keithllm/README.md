# How to setup development environment
Install develop tools: Visual Studio Code for coding on Windows 11 and Ubuntu 20.04
(https://code.visualstudio.com/)

Setup compiler environment: install fastapi for running on Windows 11 and Ubuntu 20.04
(https://fastapi.tiangolo.com/tutorial/)

Local inference ollama installation: install ollama on Windows 11 and Ubuntu 20.04 
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
3.9.19

Get up and running with large language models locally. 
install ollama (https://github.com/ollama/ollama)
$ curl -fsSL https://ollama.com/install.sh | sh

Run ollama
$ ollama run llama3

[Ubuntu22.04]
Totally new machine after install Ubuntu22.04
instal Visual Studio Code after install, select from GUI
Next,
$ sudo apt install git
$ mkdir git
$ cd git
$ git clone https://github.com/keithksleeitri/keithllmsrc.git
$ sudo apt intall net-tools (for ifconfig command)
$ sudo apt update
$ sudo apt install openssh-server (https://reintech.io/blog/setting-up-sftp-server-ubuntu-22)
$ sudo systemctl status ssh
Put your open ai key in .env file for protection, if you want to use chatgpt API.
$ python3 --version
Python 3.10.12
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install curl

Get up and running with large language models locally. 
install ollama (https://github.com/ollama/ollama)
$ curl -fsSL https://ollama.com/install.sh | sh

Run ollama
$ ollama run llama3

$ sudo apt install python3-pip -y
$ pip --version
pip 22.0.2 (python 3.10)
$ pip3 --version
pip 22.0.2 (python 3.10)

Setup Vue3 yarn to mange JavaScript runtime envrionments (https://linuxgenie.net/how-to-install-yarn-on-ubuntu-22-04/)
$ sudo apt update
$ curl --version
$ sudo apt install curl (if necessary)
$ curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - (Importing Yarn GPD Key)
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
$ sudo apt install yarn -y
$ sudo yarn --version
$ sudo atp install npm -y
$ sudo curl --compressed -o- -L https://yarnpkg.com/install.sh | bash 
Successfully install Yarn 1.22.19!
Next, install Vue.js on Ubuntu 22.04 (https://www.linuxtuto.com/how-to-install-vue-js-on-ubuntu-22-04/)
$ sudo apt update && sudo apt upgrade -y
$ sudo curl -sL https://deb.nodesource.com/setup_18.x | sudo bash - (Note that 'sudo' after pipeline is necessary for authority)
$ sudo apt remove nodejs -y
$ sudo apt autoremove
$ sudo apt install nodejs -y
$ node --version
v18.20.3
$ sudo np install npm@latest -g
$ npm --version
10.8.0
$ sudo npm install -g @vue/cli
$ vue --version
@vue/cli 5.0.8

install Docker on Ubuntu 22.04
$ sudo apt install docker.io
$ docker -v
$ sudo docker ps

docker build on windows 11
1. C:keithllmfastapi>docker build -t keithllmfastapi .
2. C:keithllmfastapi>docker run --name keithllmbackend -p 3000:3000 keithllmfastapi 
The following command for docker maintain   
3. C:keithllmfastapi>docker stop keithllmbackend
4. C:keithllmfastapi>docker rm keithllmbackend
5. C:keithllmfastapi>docker image rm keithllmfastapi
docker build on Ubuntu 22.04
   1. $ cd keithllmfastapi
   2. Put your open ai key in .env file for protection, if you want to use chatgpt API.
   3. $ sudo docker build -t keithllmfastapi .
   4. $ sudo docker run --name keithllmbackend -p 3000:3000 keithllmfastapi
   
# How to reproduce your work
You can get the up-to-date source code from git [keithksleeitri](git clone https://github.com/keithksleeitri/keithllmsrc.git)
Please change to the directory keithllmsrc
$ cd keithllmsrc
You will find this README.md file in keithllm folder.
[Ubuntu20.04]
1. Execute fast api (uvicorn main:app --reload --host 0.0.0.0 --port 3000)
   1. $ cd keithllmfastapi
   2. Put your open ai key in .env file for protection, if you want to use chatgpt API.
   3. $ pip install --upgrade pip
   4. $ pip3 install openai
   5. $ pip3 install python-decouple
   6. $ pip3 install fastapi
   7. $ pip3 install click==8.0.1
   8. $ pip3 install requests
   9. $ pip3 install bs4
   10. $ sudo apt install uvicorn -y
   11. $ uvicorn main:app --reload --host 0.0.0.0 --port 3000
[Ubuntu22.04]
1. Execute fast api (uvicorn main:app --reload --host 0.0.0.0 --port 3000)
   1. $ cd keithllmfastapi
   2. Put your open ai key in .env file for protection, if you want to use chatgpt API.
   3. $ pip install openai
   4. $ pip install python-decouple
   5. $ pip install fastapi
   6. $ pip install bs4
   7. $ sudo apt install uvicorn -y
   8. $ uvicorn main:app --reload --host 0.0.0.0 --port 3000
[Docker on Ubuntu20.04 or Ubuntu22.04]
1. Execute fast api (uvicorn main:app --reload --host 0.0.0.0 --port 3000)
   1. $ cd keithllmfastapi
   2. Put your open ai key in .env file for protection, if you want to use chatgpt API.
   3. $ sudo docker build -t keithllmfastapi .
   4. $ sudo docker run --name keithllmbackend -p 3000:3000 keithllmfastapi
   
2. Open browser [llmfrontend] (http://127.0.0.1:3000/docs)
3. Execute llmchatgpt with transcription_target_url from [SayIt](https://sayit.pdis.nat.gov.tw/speeches)
   1. for example (https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿)
4. Find the result from Response body on the browser

# Bonus
Run vue3 Frontend
1. Execute Vue3 frontend
>cd keithllmsummary
>yarn serve
2. Open browser [vuellmfrontend] (http://localhost:8080)
3. Execute llmchatgpt with transcription_target_url from [SayIt](https://sayit.pdis.nat.gov.tw/speeches)
   1. for example (https://sayit.pdis.nat.gov.tw/2024-01-04-商周一月專欄訪談唐鳳部長逐字稿)
4. Find the result from Response body on the browser. [bonus](jpg/vue3_fastapi_chatgpt.png), Apply another fastapi llmchatgpt, using the follow url (url: 'http://localhost:3000/llmchatgpt/') to call fastapi llmchatgpt, you need run 'ollama run llama3' in backend
   [bonus](jpg/vue3_fastapi_llmchatgpt_ollama.png) If no input, system sent default url for user. [bonus](jpg/vue3_fastapi_llmchatgpt_ollama_withdefaultvalue.png) 

Run vue3 Frontend on Ubuntu22.04
>cd keithllmsummary
>rm yarn.lock
>npm install
>npm run serve

# Anything can help other understanding your work
References:
1. Vue.js from entry to practice, ISBN 978-726-324-476-4, EL0258, 2023-06, [GOTOP](https://www.gotop.com.tw)
2. Python program design and OpenAI API applications, ISBN 978-626-333-643-8, MP22308, 2023-11 [DRMASTER](https://www.drmaster.com.tw)

# Contributer
The main contributer is Keith K.S. Lee keith.kslee@gmail.com

