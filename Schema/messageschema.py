from pydantic import BaseModel
from typing import Literal, List, Dict, Any


class ChatResponseFormat(BaseModel):
    type: Literal["text", "selector"]
    message: str
    selections: List[Dict[str, Any]] = []