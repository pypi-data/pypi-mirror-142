# pylint: skip-file
import pytest

from unimatrix.ext import kms
from ..registry import registry as REGISTRY


class TestRegistry:

    @pytest.fixture(scope='function')
    async def registry(self):
        await REGISTRY.register('test', ['file+pem:pki/rsa.key'], ['sig'])
        yield REGISTRY
        REGISTRY.delete('test')

    @pytest.mark.asyncio
    async def test_register_self_raises_valueeror(self, registry):
        with pytest.raises(ValueError):
            await registry.register('self', ['file+pem:pki/rsa.key'], ['sig'])

    @pytest.mark.asyncio
    async def test_register_no_versions_raises_valueeror(self, registry):
        with pytest.raises(ValueError):
            await registry.register('foo', [], ['sig'])

    @pytest.mark.asyncio
    async def test_register_duplicate_raises_valueerror(self, registry):
        with pytest.raises(ValueError):
            await registry.register('test', ['file+pem:pki/rsa.key'], ['sig'])
