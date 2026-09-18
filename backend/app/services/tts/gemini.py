from google import genai
from google.genai import types

from app.core.config import get_settings
from app.services.tts import TTSProvider

class GeminiTTSProvider(TTSProvider):
    """Gemini-backed text-to-speech provider."""
    
    def __init__(self) -> None:
        settings = get_settings()
        
        settings.gemini_tss_model