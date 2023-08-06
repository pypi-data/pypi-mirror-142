# pylint: skip-file
import os

import pytest

from unimatrix.ext import kms


ALGORITHMS = {'sha256', 'sha384', 'sha512'}


class BaseSigning:
    address = 'file+pem:pki/p256.key'
    message = b"Hello world!"
    algorithm = 'sha256'
    unsupported_signing_algorithms = {"sha224", "md5"}
    padding = None
    has_identity = True
    _signatures: dict = {}

    def get_signing_params(self) -> dict:
        return {}

    @pytest.mark.asyncio
    async def test_invoke_keyid(self, key):
        if self.has_identity:
            assert key.keyid

    @pytest.fixture(scope='function')
    async def key(self):
        await kms.keychain.register('test', self.address)
        try:
            yield kms.keychain.get('test')
        finally:
            await kms.keychain.unregister('test')

    @pytest.fixture(scope='function')
    async def signature(self, key):
        k = (key.keyid, self.message, self.algorithm, self.padding)
        if k not in BaseSigning._signatures:
            sig = await key.sign(
                data=self.message,
                algorithm=self.algorithm,
                **self.get_signing_params()
            )
            BaseSigning._signatures[k] = sig
        return BaseSigning._signatures[k]

    @pytest.mark.asyncio
    async def test_sign(self, signature):
        pass

    @pytest.mark.asyncio
    async def test_sign_with_unknown_algorithm_raises(self, key):
        with pytest.raises(kms.exceptions.UnsupportedSigningAlgorithm):
            await key.sign(self.message, algorithm='foo',
                **self.get_signing_params())

    @pytest.mark.asyncio
    async def test_sign_with_unsupported_algorithm_raises(self, key):
        if not self.unsupported_signing_algorithms:
            pytest.skip()
        for algorithm in self.unsupported_signing_algorithms:
            with pytest.raises(kms.exceptions.UnsupportedSigningAlgorithm):
                await key.sign(self.message, algorithm=algorithm,
                    **self.get_signing_params())

    @pytest.mark.asyncio
    async def test_verify_from_key_valid(self, key, signature):
        assert await key.verify(signature, self.message, algorithm=self.algorithm,
            **self.get_signing_params())

    @pytest.mark.asyncio
    async def test_verify_from_key_invalid(self, key, signature):
        assert not await key.verify(signature, os.urandom(4), algorithm=self.algorithm,
            **self.get_signing_params())
