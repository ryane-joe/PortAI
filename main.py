
from openai import OpenAI

client = OpenAI(api_key="sk-83f98f92bc3b497ab5692671acdaf6c7", base_url="https://api.deepseek.com/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "what are the vulnerabilities with ssh 5.4"},
    ],
    stream=False
)

print(response.choices[0].message.content)