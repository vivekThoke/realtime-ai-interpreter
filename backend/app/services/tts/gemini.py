from google import genai
from google.genai import types

from app.core.config import get_settings
from app.services.tts import TTSProvider


class GeminiTTSProvider(TTSProvider):
    """Gemini-backed text-to-speech provider."""

    def __init__(self) -> None:
        settings = get_settings()

        self.model = settings.gemini_tts_model
        self.voice = settings.gemini_tts_voice

        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    async def synthesize(
        self,
        text: str,
        language: str,
    ) -> bytes:
        prompt = f"""
                    Read the following text aloud naturally in {language}.

                    Text:
                    {text}
                    """.strip()

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=self.voice,
                        )
                    )
                ),
            ),
        )

        try:
            # audio_data = response.candidates[0].content.parts[0].inline_data.data
            candidates = response.candidates

            if not candidates:
                raise RuntimeError("Gemini returned no candidates.")

            content = candidates[0].content

            if content is None:
                raise RuntimeError("Gemini returned no content.")

            parts = content.parts

            if not parts:
                raise RuntimeError("Gemini returned no content parts.")

            inline_data = parts[0].inline_data

            if inline_data is None:
                raise RuntimeError("Gemini returned no inline audio data.")

            audio_data = inline_data.data

            if not audio_data:
                raise RuntimeError("Gemini returned empty audio data.")

        except (IndexError, AttributeError, TypeError) as exc:
            raise RuntimeError("Gemini returned no audio data.") from exc

        return audio_data
