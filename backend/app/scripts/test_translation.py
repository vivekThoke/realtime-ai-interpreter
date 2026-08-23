import asyncio

from app.services.translation import GeminiTranslationProvider


async def main() -> None:
    provider = GeminiTranslationProvider()

    result = await provider.translate(
        text="Where is the nearest railway station?",
        source_language="English",
        target_language="Hindi",
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())