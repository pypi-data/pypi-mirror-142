# pylint: skip-file
import pytest

from ..exceptions import InvalidSignature
from ..exceptions import TrustIssues
from ..jsonwebtoken import JSONWebToken
from .. import registry


class JOSECompatibility:

    async def run_algorithm_verify_test(self, keychain, name, algorithm, payload):
        key = keychain.get(name, private=True)
        encoded = await self.encode(
            key=key,
            algorithm=algorithm,
            payload=payload,
            headers={'kid': key.keyid}
        )
        token = JSONWebToken.decode(encoded)
        assert await token.verify_signature(keychain)

    @pytest.mark.asyncio
    async def test_verify_hs256(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='hmac',
            algorithm='HS256',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_hs384(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='hmac',
            algorithm='HS384',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_hs512(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='hmac',
            algorithm='HS512',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_rs256(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='rsa',
            algorithm='RS256',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_rs384(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='rsa',
            algorithm='RS384',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_rs512(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='rsa',
            algorithm='RS512',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_ps256(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='rsa',
            algorithm='PS256',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_ps384(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='rsa',
            algorithm='PS384',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_ps512(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='rsa',
            algorithm='PS512',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_es256(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='p256',
            algorithm='ES256',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_es384(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='p384',
            algorithm='ES384',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_verify_es512(self, keychain):
        await self.run_algorithm_verify_test(
            keychain=keychain,
            name='p521',
            algorithm='ES512',
            payload={}
        )

    @pytest.mark.asyncio
    async def test_forged_signature_hs256(self, keychain):
        key = keychain.get('hmac')
        encoded = await self.encode(
            key=None,
            secret="malicious key",
            algorithm="HS256",
            payload={'sub': 'foo'},
            headers={'kid': key.keyid}
        )
        with pytest.raises(InvalidSignature):
            token = JSONWebToken.decode(encoded)
            await token.verify_signature(keychain)
