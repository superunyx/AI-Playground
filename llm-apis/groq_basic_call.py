"""Basic LLM API call using the Groq SDK."""

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Error: GROQ_API_KEY not found in environment variables.")

# Initialize Groq client
client = Groq(api_key=my_api_key)

# Specify model and prompt
model = "openai/gpt-oss-20b"
role = "user"
prompt = "This is a test call"

message = {
    "role": role,
    "content": prompt,
}

messages = [message]

# Execute chat completion
response = client.chat.completions.create(model=model, messages=messages)

print("Raw Response:")
print(response)

print("\n" + "=" * 40 + "\n")

answer = response.choices[0].message.content
print("Extracted Content:")
print(answer)
