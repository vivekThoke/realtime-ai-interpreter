import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_translation_service
from app.main import app
from app.services.translation.service import TranslationService


class FakeTranslationProvider:
    async def translate(
        self,
        text: str,
        source_language: str,
        target_language: str,
    ) -> str:
        return "निकटतम रेलवे स्टेशन कहाँ है?"


def get_fake_translation_service() -> TranslationService:
    return TranslationService(
        provider=FakeTranslationProvider(),
    )


@pytest.fixture
def client() -> TestClient:
    app.dependency_overrides[get_translation_service] = get_fake_translation_service

    yield TestClient(app)

    app.dependency_overrides.clear()


def test_translate(client: TestClient) -> None:
    response = client.post(
        "/api/v1/translate",
        json={
            "text": "Where is the nearest railway station?",
            "source_language": "English",
            "target_language": "Hindi",
        },
    )

    assert response.status_code == 200
    assert response.json()["translated_text"] == ("निकटतम रेलवे स्टेशन कहाँ है?")


def test_translate_rejects_empty_text(
    client: TestClient,
) -> None:
    response = client.post(
        "/api/v1/translate",
        json={
            "text": "",
            "source_language": "English",
            "target_language": "Hindi",
        },
    )

    assert response.status_code == 422
