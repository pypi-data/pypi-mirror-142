# pylint: skip-file
import pytest

from ..jsonwebkeyset import JSONWebKeySet


class TestJSONWebKeySet:

    def test_parse_json(self, jwks_json):
        jwks = JSONWebKeySet.fromjson(jwks_json)
        assert len(jwks) == 2

    def test_parse_json_bytes(self, jwks_json):
        jwks = JSONWebKeySet.fromjson(jwks_json.encode("utf-8"))
        assert len(jwks) == 2

    def test_parse_dict(self, jwks_dict):
        jwks = JSONWebKeySet.fromdict(jwks_dict)
        assert len(jwks) == 2

    @pytest.mark.asyncio
    async def test_verify_valid(self, jwks, signature, message):
        assert await jwks.verify(
            signature=signature,
            payload=message,
            using='d63dbe73aad88c854de0d8d6c014c36dc25c4292'
        )

    @pytest.mark.asyncio
    async def test_verify_valid_no_kid(self, jwks, signature, message):
        assert await jwks.verify(signature, message)

    @pytest.mark.asyncio
    async def test_verify_unknown_kid_is_not_valid(self, jwks, signature, message):
        assert not await jwks.verify(
            signature=signature,
            payload=message,
            using='d63dbe73aad88c854de0d8d6c014c36dc25c4292+foo'
        )

    @pytest.mark.asyncio
    async def test_verify_invalid_payload_is_not_valid(self, jwks, signature, message):
        assert not await jwks.verify(
            signature=signature,
            payload=b'goo'
        )

    @pytest.mark.asyncio
    async def test_verify_invalid_signature_is_not_valid(self, jwks, signature, message):
        assert not await jwks.verify(
            signature=b'foo',
            payload=message
        )

    @pytest.mark.asyncio
    async def test_verify_mismatching_preset_is_not_valid(self, jwks, signature, message):
        assert not await jwks.verify(
            signature=signature,
            payload=message,
            algorithm='HS256'
        )
