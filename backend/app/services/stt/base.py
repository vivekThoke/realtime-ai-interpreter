from abc import ABC, abstractmethod

class STTProvider(ABC):
    """Interface for speech-to-text providers."""
    
    @abstractmethod
    async def transcribe(
        self,
        audio: bytes,
        filename: str,
        language: str,
    ) -> str:
        """Convert audio to text."""
        raise NotImplementedError