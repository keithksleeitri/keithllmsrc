# To install package
# pip3 install openai
# pip3 instal python-decoupe
from openai import OpenAI
from decouple import config

client = OpenAI(api_key=config('OPENAI_API_KEY'))

print("請稍待 ...")

message = "台北那裡最好玩?"

completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
  {"role": "system", "content": "你會說中文, 是聰明的助理"},
  {"role": "user", "content": message}
])

response=completion.choices[0].message.content
print(response)

