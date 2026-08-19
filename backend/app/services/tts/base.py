from abc import ABC, abstractmethod

class TTSProvider(ABC):
    """Interface for tex-to-speech providers."""
    
    @abstractmethod
    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> bytes:
        """Convert text to audio."""
        raise NotImplementedError