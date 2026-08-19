from pydantic import BaseModel, Field


class LanguagePair(BaseModel):
    source_language: str = Field(min_length=2, max_length=10)
    target_language: str = Field(min_length=2, max_length=10)
