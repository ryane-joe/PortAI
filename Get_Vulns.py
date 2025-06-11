
from openai import OpenAI
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))
client = OpenAI(api_key=os.getenv("api_key"), base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "what are the vulnerabilities with ssh 5.4"},
    ],
    stream=False
)

print(response.choices[0].message.content)