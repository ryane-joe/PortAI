from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))

client = OpenAI(
    api_key=os.getenv("api_key"),
    base_url="https://api.deepseek.com/v1"
)

def get_vulnerabilities(service: str) -> str:
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a cybersecurity assistant that specializes in vulnerability detection. "
                        "When the user provides the name and version of a software or service, "
                        "you return a list of known CVEs associated with it, including their CVE ID, severity, "
                        "description, and publication date. Be concise and factual. you will not give any end output like let me know if you need specific infomation etc, it will be concise to just the cve information"
                    )
                },
                {"role": "user", "content": f"What are the vulnerabilities with {service}?"},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error retrieving vulnerabilities for {service}: {e}"
