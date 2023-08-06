# pylint: skip-file
import pytest

from ..keyversion import KeyVersion


class TestKeyVersion:

    @pytest.mark.asyncio
    async def test_fromurl_raises_with_invalid_scheme(self):
        with pytest.raises(ValueError):
            await KeyVersion.fromurl('foo:pki/rsa.key')

    @pytest.mark.asyncio
    async def test_fromurl_raises_with_missing_scheme(self):
        with pytest.raises(ValueError):
            await KeyVersion.fromurl('pki/rsa.key')

    @pytest.mark.asyncio
    async def test_fromurl_raises_with_from_platform(self):
        with pytest.raises(ValueError):
            await KeyVersion.fromurl('cloud://foo.com/rsa.key')
