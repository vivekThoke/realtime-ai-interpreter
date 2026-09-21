from functools import lru_cache

from app.services.stt import GeminiSTTProvider, STTProvider
from app.services.stt.service import STTService
from app.services.translation import (
    GeminiTranslationProvider,
    TranslationProvider,
)
from app.services.translation.service import TranslationService
from app.services.tts import GeminiTTSProvider, TTSProvider
from app.services.tts.service import TTSService


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


@lru_cache
def get_tts_provider() -> TTSProvider:
    return GeminiTTSProvider()


@lru_cache
def get_tts_service() -> TTSService:
    return TTSService(
        provider=get_tts_provider(),
    )
