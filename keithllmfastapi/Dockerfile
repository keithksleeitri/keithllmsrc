FROM python:3.9

RUN apt-get update
WORKDIR /usr/src
COPY . /usr/src
RUN pip install --upgrade pip
RUN pip install openai
RUN pip install python-decouple
RUN pip install fastapi
RUN pip install bs4
RUN pip install requests
RUN pip install click==8.0.1
RUN apt install uvicorn -y

EXPOSE 3000

CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","3000"]