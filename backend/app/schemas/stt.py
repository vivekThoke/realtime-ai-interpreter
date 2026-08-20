from pydantic import BaseModel


class TranscriptionResponse(BaseModel):
    language: str
    text: str