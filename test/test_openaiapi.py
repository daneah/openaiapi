import pytest

from openaiapi import OpenAI


def test_api_domain():
    assert OpenAI.domain == "https://api.openai.com"


def test_required_headers(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "supersecret")
    assert OpenAI.required_headers == {"Authorization": "Bearer supersecret"}


def test_required_headers_when_no_api_key(monkeypatch):
    with pytest.raises(RuntimeError):
        OpenAI.required_headers
