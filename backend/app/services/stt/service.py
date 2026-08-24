from app.services.stt import STTProvider

class STTService:
    """Application service for speech-to-text"""
    
    def __init__(self, provider: STTProvider) -> None:
        self.provider = provider
        
    async def transcribe(
        self,
        audio: bytes,
        filename: str,
        language: str
    ) -> str:
        return await self.provider.transcribe(
            audio=audio,
            filename=filename,
            language=language
        )