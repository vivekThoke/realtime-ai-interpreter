from abc import ABC, abstractmethod


class TranslationProvider(ABC):
    """Interface for translation providers."""

    @abstractmethod
    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:
        """Translate text between languages."""
        raise NotImplementedError
