from pydantic import BaseModel


class Language(BaseModel):
    code: str
    name: str


class LanguagePair(BaseModel):
    source_language: str
    target_language: str
