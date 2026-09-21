import asyncio
import wave
from pathlib import Path

from app.services.tts import GeminiTTSProvider

def save_wav(
    path: Path,
    pcm_data: bytes,
    channels: int = 1,
    sample_rate: int = 24000,
    sample_width: int = 2,
) -> None:
    with wave.open(str(path), "wb") as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm_data)
        

async def main() -> None:
    provider = GeminiTTSProvider()

    audio = await provider.synthesize(
        text="निकटतम रेलवे स्टेशन कहाँ है?",
        language="Hindi",
    )

    output_path = Path("output.wav")
    save_wav(output_path, audio)

    print(f"Audio written to: {output_path.resolve()}")
    

if __name__ == "__main__":
    asyncio.run(main())