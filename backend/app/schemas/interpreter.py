from pydantic import BaseModel


class InterpretationResponse(BaseModel):
    source_language: str
    target_language: str
    transcript: str
    translation: str
