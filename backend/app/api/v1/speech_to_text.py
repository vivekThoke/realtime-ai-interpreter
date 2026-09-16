from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status
)

from app.api.dependencies import get_stt_service
from app.schemas.stt import TranscriptionResponse
from app.services.stt.service import STTService


router = APIRouter(
    prefix="/speech-to-text",
    tags=["Speech-to-Text"]
)

@router.post(
    "",
    response_model=TranscriptionResponse
)
async def speech_to_text(
    audio: UploadFile = File(...),
    language: str = Form("English"),
    service: STTService = Depends(get_stt_service),
) -> TranscriptionResponse:
    if not audio.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Audio filename is required."
        )
        
    try:
        audio_bytes = await audio.read()
        
        if not audio_bytes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Audio file is empty."
            )
            
        transcript = await service.transcribe(
            audio_bytes,
            audio.filename,
            language
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        ) from exc
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Speech-to-text provider request failed: {exc}",
        ) from exc
        
    return TranscriptionResponse(
        language=language,
        text=transcript
    )