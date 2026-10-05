## basic program to count respons tokens count them and see how total 
## tokens are counted and also how to limit them using max_tokens

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

prompt1="Hi!"
prompt2="Explain time travel in detail."
prompt3="Write an 1000 word essay on machine learning"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
            "role":role,
            "content":prompt
            }
    messages=[message]
    response = client.chat.completions.create(model=model,messages=messages,max_tokens=50)
    print("#############################")
    usage=response.usage
    print(f"Prompt: {prompt} --> yourtokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens:{usage.total_tokens} Finish Reason:{response.choices[0].finish_reason}")

