# pylint: skip-file
import pytest

from unimatrix.ext import kms


class TestExplicitKeyIdentifier:

    @pytest.mark.asyncio
    async def test_keyid_as_parameter_hmac(self, keychain):
        hmac = keychain.get('hmac')
        assert hmac.keyid == 'hmac'
