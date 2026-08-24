from google import genai
from google.genai import types

from app.core.config import get_settings
from app.services.stt import STTProvider


class GeminiSTTProvider(STTProvider):
    """Gemini-backed speech-to-text provider."""

    def __init__(self) -> None:
        settings = get_settings()

        self.model = settings.gemini_stt_model
        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    async def transcribe(
        self,
        audio: bytes,
        filename: str,
        language: str,
    ) -> str:
        mime_type = self._get_mime_type(filename)

        prompt = (
            "Transcribe the speech in this audio file.\n\n"
            f"The expected spoken language is {language}.\n"
            "Return only the transcript.\n"
            "Do not add explanations, labels, timestamps, or quotation marks."
        )

        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=audio,
                    mime_type=mime_type,
                ),
            ],
        )

        transcript = response.text

        if not transcript:
            raise RuntimeError("Gemini returned an empty transcript.")

        return transcript.strip()

    @staticmethod
    def _get_mime_type(filename: str) -> str:
        extension = filename.lower().rsplit(".", 1)[-1]

        mime_types = {
            "wav": "audio/wav",
            "mp3": "audio/mp3",
            "mpeg": "audio/mpeg",
            "aac": "audio/aac",
            "ogg": "audio/ogg",
            "flac": "audio/flac",
        }

        try:
            return mime_types[extension]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported audio format: .{extension}"
            ) from exc