from google import genai

from app.core.config import get_settings
from app.services.translation import TranslationProvider

class GeminiTranslationProvider(TranslationProvider):
    """Gemini-backed translation provider"""
    
    def __init__(self) -> None:
        settings = get_settings()
        
        self.model = settings.gemini_translation_model
        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )
        
    async def translate(
        self, 
        text, 
        source_language, 
        target_language
    ) -> str:
        prompt = (
            "Translate the following text from"
            f"{source_language} to {target_language}.\n\n"
            "Rules:\n"
            "- Return only tranlsation.\n"
            "- Do not explain the translation.\n"
            "- Preserve original meaning.\n"
            "- Don't add quotation marks.\n\n"
            f"Text: \n{text}"
        )
        
        response = self.client.aio.model.generate_content(
            model=self.model,
            content=prompt,
        )
        
        translated_text = response.text
        
        if not translated_text:
            raise RuntimeError("Gemini returned an empty translation.")
        
        return translated_text.strip()
        
        

