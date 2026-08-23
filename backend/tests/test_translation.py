import pytest

from app.services.translation import TranslationProvider


class FakeTranslationProvider(TranslationProvider):
    async def translate(
        self, 
        text, 
        source_language, 
        target_language
    ) -> str:
        return "निकटतम रेलवे स्टेशन कहाँ है?"
    
@pytest.mark.asyncio
async def test_translation_provider_contract() -> None:
    provider = FakeTranslationProvider()
    
    result = await provider.translate(
        text="Where is nearest railway station?",
        source_language="English",
        target_language="Hindi"
    )       
    
    assert result == "निकटतम रेलवे स्टेशन कहाँ है?"