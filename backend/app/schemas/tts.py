from pydantic import BaseModel

class SpeechSynthesisRequest(BaseModel):
    text: str   
    language: str