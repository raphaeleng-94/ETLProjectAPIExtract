import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "Olá, Qual é o preço do Etherum atualmente?"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json()["choices"][0]["message"]["content"])






