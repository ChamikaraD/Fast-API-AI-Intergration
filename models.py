
from typing import List, Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str


class LlmResponseSchema(BaseModel):
    persona: str
    content: str
    tips: Optional [List[str]] = None

