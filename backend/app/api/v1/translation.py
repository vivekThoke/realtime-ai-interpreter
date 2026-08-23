from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_translation_service
from app.schemas.translation import (
    TranslationRequest,
    TranslationResponse,
)
from app.services.translation.service import TranslationService

router = APIRouter(
    prefix="/translate",
    tags=["Translation"] 
)

@router.post(
    "",
    response_model=TranslationResponse,
)
async def translate(
    request: TranslationRequest,
    service: TranslationService = Depends(get_translation_service)
) -> TranslationResponse:
    try: 
        translated_text = await service.translate(
            text=request.text,
            source_language=request.source_language,
            target_language=request.target_language
        )
    except ValueError as exec:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exec)
        ) from exec
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Translation provider request failed.",
        ) from exec
    
    return TranslationResponse(
        source_language=request.source_language,
        target_language=request.target_language,
        source_text=request.text,
        translated_text=translated_text,
    )