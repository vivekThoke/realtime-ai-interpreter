from app.services.stt import STTProvider
from app.services.translation import TranslationProvider
from app.services.tts import TTSProvider


class InterpreterService:
    """Coordinates the MVP speech translation pipleine"""

    def __inti__(
        self,
        stt_provider: STTProvider,
        translation_provider: TranslationProvider,
        tts_provider: TTSProvider,
    ) -> None:
        self.stt_provider = stt_provider
        self.translation_provider = translation_provider
        self.tss_provider = tts_provider

    async def interpret(
        self,
        audio: bytes,
        filename: str,
        source_language: str,
        target_language: str,
    ) -> tuple[str, str, bytes]:

        transcript = await self.stt_provider.transcribe(
            audio=audio,
            filename=filename,
            language=source_language,
        )

        translated_text = await self.translation_provider.translate(
            text=transcript,
            source_language=source_language,
            target_language=target_language,
        )

        translated_audio = await self.tss_provider.synthesize(
            translated_text, language=target_language
        )

        return transcript, translated_text, translated_audio
