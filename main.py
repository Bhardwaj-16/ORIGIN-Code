from openrouter import OpenRouter
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("HCAPI")

client = OpenRouter(
    api_key = api,
    server_url = "https://ai.hackclub.com/proxy/v1",
)

prompt = input(">>> ")

response = client.chat.send(
    model = "x-ai/grok-4.1-fast",
    messages = [
        {"role": "user", "content": f"{prompt}"}
    ],
    stream = False,
)

print(response.choices[0].message.content)