import requests
import json

url= "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2:1b",
    "messages":[
    {"role": "System", "content": "You are a pirate and you also talk like one"},
    {"role": "user", "content": "Whats the capital of Germany?"},
    ],
    "options": {
        "temperature": 1
    }
}

response = requests.post(url, json=payload, stream=True)

full_response = ""
for line in response.iter_lines():
    if line:
        decoded = line.decode("utf-8")
        chunk = json.loads(decoded)
        content = chunk.get("message", {}).get("content", "")
        full_response += content
        if chunk.get("done", False):
            break

print(full_response)