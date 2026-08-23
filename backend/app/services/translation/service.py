from app.services.translation import TranslationProvider


class TranslationService:
    """Application service for text translation."""

    def __init__(self, provider: TranslationProvider) -> None:
        self.provider = provider

    async def translate(
        self, text: str, source_language: str, target_language: str
    ) -> str:
        return await self.provider.translate(
            text=text, source_language=source_language, target_language=target_language
        )
