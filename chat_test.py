import ollama
from ollama import Client

client = Client(host="http://localhost:11434")

prompt = input("You:")
response = client.chat(model="concise-pi", messages=[
    {
        "role": "user",
        "content": prompt
    }
])

print(response.message.content)
