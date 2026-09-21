import pytest

from app.services.tts import TTSProvider


class FakeTTSProvider(TTSProvider):
    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> bytes:
        return b"fake-audio"


@pytest.mark.asyncio
async def test_tts_provider_contract() -> None:
    provider = FakeTTSProvider()

    result = await provider.synthesize(
        text="नमस्ते",
        language="Hindi",
    )

    assert result == b"fake-audio"
