import requests
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import Client

LOCAL_MODEL_URL = os.getenv("LOCAL_MODEL_URL", "http://localhost:11434/")

app = FastAPI(title="Concise-Pi API", version="0.1")
client = Client(host="http://localhost:11434")

class AskRequest(BaseModel):
    query: str


def query_local_model(prompt: str) -> str:
    try:
        response = client.chat(model="concise-pi", messages=[
            {
                "role": "user",
                "content": prompt
            }
        ])
        return response.message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Local model error: {e}")


@app.post("/ask")
def ask(req: AskRequest):
    user_query = req.query.strip()
    full_prompt = f"User: {user_query}\nAssistant:"
    answer = query_local_model(full_prompt)
    return {"answer": answer}
