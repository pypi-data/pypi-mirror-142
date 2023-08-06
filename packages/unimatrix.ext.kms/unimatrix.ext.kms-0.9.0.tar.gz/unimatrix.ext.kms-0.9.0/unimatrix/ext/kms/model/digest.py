"""Declares :class:`Digest`."""
import inspect
import pathlib
import typing

import aiofiles
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hashes import SHA384
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.primitives import hashes


HASH_MAPPING = {
    'sha256': SHA256,
    'sha384': SHA384,
    'sha512': SHA512,
}


class Digest:
    """Represents a message digest."""

    @staticmethod
    def get_hasher(algorithm: str):
        return HASH_MAPPING[algorithm]()

    @property
    def algorithm(self) -> typing.Union[SHA256, SHA384, SHA512]:
        """Return the hashing algorithm used to create the digest."""
        return self.get_hasher(self._algorithm)

    @classmethod
    async def fromfile(cls,
        algorithm: str,
        f: typing.Union[pathlib.Path, str, typing.BinaryIO]
    ):
        """Create a new :class:`Digest` from a file. The `f` parameter may
        either be a string pointing a file, or a file-like object.
        """
        hasher = hashes.Hash(cls.get_hasher(algorithm))
        if isinstance(f, (pathlib.Path, str)):
            f = await aiofiles.open(str(f), 'rb').__aenter__()
        f.seek(0)
        while True:
            buf = f.read(1024)
            if inspect.isawaitable(buf):
                buf = await buf
            if not buf:
                break
            hasher.update(buf)
        return cls(algorithm=algorithm, digest=hasher.finalize())


    def __init__(self, algorithm: str, message: bytes = None, digest: bytes = None):
        if not (bool(message) ^ bool(digest)):
            raise TypeError("Only one of `message` or `digest` must be None.")
        self._algorithm = algorithm
        self._digest = digest
        self._message = message

    def __bytes__(self) -> bytes:
        if self._digest is None:
            hasher = hashes.Hash(self.algorithm)
            hasher.update(self._message)
            self._digest = hasher.finalize()
        return self._digest

    def __eq__(x, y) -> bool:
        return bytes(x) == bytes(y)
