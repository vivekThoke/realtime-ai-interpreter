import io

import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_stt_service
from app.main import app
from app.services.stt.service import STTService


class FakeSTTProvider:
    async def transcribe(
        self,
        audio: bytes,
        filename: str,
        language: str,
    ) -> str:
        assert audio == b"fake-audio"
        assert filename == "sample.wav"
        assert language == "English"

        return "Where is the nearest railway station?"


def get_fake_stt_service() -> STTService:
    return STTService(
        provider=FakeSTTProvider(),
    )


@pytest.fixture
def client() -> TestClient:
    app.dependency_overrides[get_stt_service] = get_fake_stt_service

    yield TestClient(app)

    app.dependency_overrides.clear()


def test_speech_to_text(client: TestClient) -> None:
    response = client.post(
        "/api/v1/speech-to-text",
        files={
            "audio": (
                "sample.wav",
                io.BytesIO(b"fake-audio"),
                "audio/wav",
            ),
        },
        data={
            "language": "English",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "language": "English",
        "text": "Where is the nearest railway station?",
    }


def test_speech_to_text_rejects_empty_file(
    client: TestClient,
) -> None:
    response = client.post(
        "/api/v1/speech-to-text",
        files={
            "audio": (
                "sample.wav",
                io.BytesIO(b""),
                "audio/wav",
            ),
        },
        data={
            "language": "English",
        },
    )

    assert response.status_code == 400
