from typing import List
from pydantic import BaseModel

class EmailModel(BaseModel):
    recipient: List[str]
    subject: str
    content: str
