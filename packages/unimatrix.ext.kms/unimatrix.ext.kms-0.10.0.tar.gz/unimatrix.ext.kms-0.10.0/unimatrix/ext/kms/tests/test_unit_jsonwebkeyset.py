# pylint: skip-file
import pytest

from ..exceptions import InvalidSignature
from ..loaders import JWKSLoader
from ..jsonwebkeyset import JSONWebKeySet


class TestJSONWebKeySet:

    @pytest.mark.asyncio
    async def test_verify_valid(self, jwks, jws):
        assert await jws.verify_signature(jwks)

    @pytest.mark.asyncio
    async def test_verify_missing_keys(self, jws):
        jwks = JSONWebKeySet()
        with pytest.raises(InvalidSignature):
            assert await jws.verify_signature(jwks)

    def test_add(self):
        x = JSONWebKeySet()
        y = JSONWebKeySet()
        assert len(x + y) == (len(x) + len(y))

    #@pytest.mark.asyncio
    #async def test_loader_discover(self):
    #    loader = JWKSLoader()
    #    jwks = await loader.discover("https://accounts.google.com")
