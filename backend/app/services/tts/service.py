from app.services.tts import TTSProvider

class TTSService:
    """Application service for text-to-speech."""
    
    def __init__(self, provider: TTSProvider) -> None:
        self.provider = provider
        
    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> bytes:
        return await self.provider.synthesize(
            text=text,
            language=language
        )