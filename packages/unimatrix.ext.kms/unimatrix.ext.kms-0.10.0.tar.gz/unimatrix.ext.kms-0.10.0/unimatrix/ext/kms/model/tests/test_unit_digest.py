# pylint: skip-file
import io
import pathlib
import tempfile

import pytest

from ..digest import Digest


class TestDigest:

    def test_message_and_digest_raises_typeerror(self):
        with pytest.raises(TypeError):
            Digest('sha256', message=b'bar', digest=b'baz')

    def test_message_and_not_digest_raises_typeerror(self):
        with pytest.raises(TypeError):
            Digest('sha256', message=None, digest=None)

    @pytest.mark.asyncio
    async def test_digest_from_file_string(self):
        with tempfile.NamedTemporaryFile('wb') as f:
            f.write(b'Hello world!')
            f.seek(0)
            digest = await Digest.fromfile('sha256', f.name)
            assert digest == Digest('sha256', b'Hello world!')

    @pytest.mark.asyncio
    async def test_digest_from_file_path(self):
        with tempfile.NamedTemporaryFile('wb') as f:
            f.write(b'Hello world!')
            f.seek(0)
            digest = await Digest.fromfile('sha256', pathlib.Path(f.name))
            assert digest == Digest('sha256', b'Hello world!')

    @pytest.mark.asyncio
    async def test_digest_from_file_sha256(self):
        f = io.BytesIO(b'Hello world!')
        digest = await Digest.fromfile('sha256', f)
        assert digest == Digest('sha256', b'Hello world!')

    @pytest.mark.asyncio
    async def test_digest_from_file_sha384(self):
        f = io.BytesIO(b'Hello world!')
        digest = await Digest.fromfile('sha384', f)
        assert digest == Digest('sha384', b'Hello world!')

    @pytest.mark.asyncio
    async def test_digest_from_file_sha512(self):
        f = io.BytesIO(b'Hello world!')
        digest = await Digest.fromfile('sha512', f)
        assert digest == Digest('sha512', b'Hello world!')
