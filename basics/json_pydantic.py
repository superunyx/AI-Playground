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

#structure

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
        "type":"json_object"
        }

system_prompt=f"""
Extract the information from the ticket based on this schema {schema} and give me in json format
"""

message_system={
        "role":"system",
        "content":system_prompt
        }


text="Hello My name in John. I have purchased an iphone which has stopped working at all. My address is Delhi. My email is john@gmail.com. My contact is 180018001800"

prompt=f"""
This is a customer ticket. Please extract the personal information from this {text}

"""

message={
        "role":role,
        "content":prompt
        }

messages=[message_system,message]

response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)

answer=response.choices[0].message.content
#print(answer)

# how to read this 

import json
raw_json=answer

data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
