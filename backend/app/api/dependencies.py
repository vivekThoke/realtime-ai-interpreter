from functools import lru_cache

from app.services.stt import GeminiSTTProvider, STTProvider
from app.services.stt.service import STTService
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


@lru_cache
def get_stt_provider() -> STTProvider:
    return GeminiSTTProvider()


@lru_cache
def get_stt_service() -> STTService:
    return STTService(
        provider=get_stt_provider(),
    )
