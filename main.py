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
            "Authorization": "Bearer <OPENROUTER_API_KEY>",
            "Content-Type": "application/json",

        }

    body = {
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages":[
                {
                    "role": "user",
                    "content": message
                }
            ]
    }
    response = requests.post(url=OPENROUTER_URL,headers=header,json=body)
    return response.json()






@app.post("/chat")
def chat(request: ChatRequest):
    pass