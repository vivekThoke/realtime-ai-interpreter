import pytest
from pydantic import ValidationError

from app.schemas import TranslationRequest


def test_translation_request() -> None:
    request = TranslationRequest(
        text="where is railway station?", source_language="en", target_language="hi"
    )

    assert request.text == "where is railway station?"
    assert request.source_language == "en"
    assert request.target_language == "hi"


def test_translation_request_rejects_empty_text() -> None:
    with pytest.raises(ValidationError):
        TranslationRequest(text="", source_language="en", target_language="hi")
