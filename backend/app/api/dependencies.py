from functools import lru_cache

from app.services.translation import (
    GeminiTranslationProvider,
    TranslationProvider,
)
from app.services.translation.service import TranslationService


@lru_cache
def get_translation_provider() -> TranslationProvider:
    return GeminiTranslationProvider()


@lru_cache
def get_translation_service() -> TranslationService:
    return TranslationService(
        provider=get_translation_provider(),
    )
