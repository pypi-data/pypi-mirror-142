"""Declares :class:`VersionedKey`."""
import asyncio
import functools
import operator
import typing

from .keyversion import KeyVersion


class VersionedKey:
    """Represents a named key that is maintained in the internal registry of the
    :mod:`unimatrix.ext.kms` package.
    """
    __module__: str = 'unimatrix.ext.kms'

    @property
    def keyid(self) -> str:
        """Return as string that uniquely identifies the key based on
        implementation-specific variable (e.g. ``x`` and ``y`` for elliptic
        curve keypairs, ``n`` and ``e`` for RSA keypairs).
        """
        return self._default.keyid

    @property
    def secret(self) -> bytes:
        return self._default.secret

    @classmethod
    async def fromversions(cls,
        versions: typing.List[str],
        usage: typing.List[str]
    ):
        """Instantiate a new :class:`VersionedKey` from a list of versions and
        specified usage.
        """
        results = await asyncio.gather(*[
            KeyVersion.fromurl(x) for x in versions
        ])
        return cls(
            versions=functools.reduce(operator.add, results),
            usage= usage
        )

    def __init__(self,
        versions: typing.List[KeyVersion],
        usage: typing.List[str]
    ):
        """Instantiate a new :class:`VersionedKey` from a list of versions."""
        self._default, *self._versions = versions
        self._usage = usage

    def get_secret(self) -> bytes:
        """If the secret for the :class:`VersionedKey` is available, return it
        as a byte-string.
        """
        return self._default.get_secret()

    async def sign(self, *args, **kwargs) -> bytes:
        """Sign `data` using the default key and the given algorithm."""
        return await self._default.sign(*args, **kwargs)

    async def verify(self, *args, **kwargs) -> bool:
        """Verifies that `sig` was created from `data` using this key."""
        return await self._default.verify(*args, **kwargs)

    async def load(self) -> None:
        """Loads metadata for all key versions. This method is typically
        invoked when registering a new key.
        """
        await self._default.load()
        await asyncio.gather(*[v.load() for v in self._versions])

    def __iter__(self):
        return iter([self._default] + self._versions)
