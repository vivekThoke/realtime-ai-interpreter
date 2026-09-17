import pytest

from app.services.stt import STTProvider


class FakeSTTProvider(STTProvider):
    async def transcribe(self, audio, filename, language) -> str:
        return "Where is nearest railway station?"


@pytest.mark.asyncio
async def test_stt_provider_contract() -> None:
    provider = FakeSTTProvider()

    result = await provider.transcribe(
        audio=b"fake-audio", filename="sample.wav", language="English"
    )

    assert result == "Where is nearest railway station?"
