import json
import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI

from models import ChatRequest

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
OPENROUTER_URL = os.getenv("OPENROUTER_URL")


app = FastAPI(title="AI Wrapper for openrouter API")

def call_openrouter_api(message:str):

    header = {
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"

        }

    body = {
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages":[
                {"role": "system", "content": " You are an Helpful AI Assistant," 
                                              "Who gives travel recommendations" 
                                              "on eco-friendly places in Srilanka"
                                              "You should refuse and "
                                              "say you are not allowed to do that"},

                { "role": "user", "content": message}
            ]
    }
    response = requests.post(url=OPENROUTER_URL,headers=header,json=body)
    return response.json()["choices"][0]["message"]["content"]


@app.post("/chat")
def chat(request: ChatRequest):
    return call_openrouter_api(request.message)