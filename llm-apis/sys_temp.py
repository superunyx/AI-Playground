import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Api Error")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"

role="user"

prompt="Suggest a name for our brand, in one word, just answer in one word and give only one name suggestion"
#SYSTEM
message_system={
        "role":"system",
        "content":"You are a brand manager for my food brand"
        }

message={
        "role":role,
        "content":prompt
        }

messages=[message_system,message]
# temp by default is 0
response = client.chat.completions.create(model=model,messages=messages,temperature=2)
#print(response)

print("#############################")
answer=response.choices[0].message.content
print(answer)
