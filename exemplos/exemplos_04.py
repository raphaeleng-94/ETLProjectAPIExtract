import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openai.com/v1/chat/completions"

openai_api_key = os.getenv("OPEN_AI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Olá, Qual é o preço do Etherum atualmente?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json()["choices"][0]["message"]["content"])






