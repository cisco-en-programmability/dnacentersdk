# -*- coding: utf-8 -*-

from unittest.mock import Mock

from dnacentersdk.api.custom_caller import CustomCaller
from dnacentersdk.restsession import RestSession


class DummyResponse:
    def __init__(self, status_code=200, text='{"ok": true}'):
        self.status_code = status_code
        self.text = text


def _make_session():
    token_calls = {"count": 0}

    def _get_token():
        token_calls["count"] += 1
        return f"token-{token_calls['count']}"

    session = RestSession(
        get_access_token=_get_token,
        base_url="https://example.com",
        version="3.1.6.0",
        user_agent="dnacentersdk",
    )
    session._ensure_authenticated()
    return session


def test_call_api_does_not_send_session_header_snapshot():
    session = _make_session()
    custom_caller = CustomCaller(session, lambda _name, payload: payload)

    captured_kwargs = {}

    def _request(method, path, expected_codes, custom_refresh, **kwargs):
        captured_kwargs.update(kwargs)
        return DummyResponse()

    session.request = Mock(side_effect=_request)

    result = custom_caller.call_api("GET", "/dna/intent/api/v1/network-device/count")

    assert result["ok"] is True
    assert "headers" not in captured_kwargs


def test_call_api_passes_only_user_headers_when_provided():
    session = _make_session()
    custom_caller = CustomCaller(session, lambda _name, payload: payload)

    captured_kwargs = {}

    def _request(method, path, expected_codes, custom_refresh, **kwargs):
        captured_kwargs.update(kwargs)
        return DummyResponse()

    session.request = Mock(side_effect=_request)

    custom_caller.call_api(
        "GET",
        "/dna/intent/api/v1/network-device/count",
        headers={"X-Custom": "value"},
    )

    assert captured_kwargs["headers"] == {"X-Custom": "value"}
