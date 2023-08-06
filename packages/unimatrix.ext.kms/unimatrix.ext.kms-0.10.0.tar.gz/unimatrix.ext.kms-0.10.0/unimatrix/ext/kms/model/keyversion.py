"""Declares :class:`KeyVersion`."""
import importlib
import types
import urllib.parse

from unimatrix.lib import http

from ..exceptions import UnsupportedSigningAlgorithm
from .digest import Digest


DEFAULT_PROVIDERS = {
    'cloud+google': 'unimatrix.ext.kms.providers.google',
    'file+pem': 'unimatrix.ext.kms.providers.pem',
    'literal+hmac': 'unimatrix.ext.kms.providers.octet',
}

VALID_SCHEMES = list(dict.keys(DEFAULT_PROVIDERS))

PLATFORMS = {'', 'cloud.google.com', 'azure.microsoft.com'}


class KeyVersion:
    """Represents a specific version of a cryptographic key."""
    __module__: str = 'unimatrix.ext.kms'

    @property
    def keyid(self) -> str:
        """Return as string that uniquely identifies the key based on
        implementation-specific variable (e.g. ``x`` and ``y`` for elliptic
        curve keypairs, ``n`` and ``e`` for RSA keypairs).
        """
        return self._keyid or self._key.keyid

    @property
    def secret(self) -> bytes:
        return self._key.secret

    @classmethod
    async def fromurl(cls, url: str) -> list:
        """Instantiate a new :class:`KeyVersion` from a URL."""
        scheme, platform, path, _, qs, *_ = urllib.parse.urlparse(url)
        if scheme not in VALID_SCHEMES:
            raise ValueError(f'Invalid scheme: {scheme}')
        provider=importlib.import_module(DEFAULT_PROVIDERS[scheme])
        params = http.parse_qs(qs)

        # An address may represent multiple key versions, such as is the case
        # with cloud KMS systems, so we need to expand the address to the actual
        # list of key addresses.
        if hasattr(provider, 'expand_path'): # pragma: no cover
            versions = await provider.expand_path(path)
        else:
            versions = [path]
        return [
            cls(provider=provider, path=x, platform=platform, scheme=scheme, **params)
            for x in versions
        ]

    def __init__(self, provider: types.ModuleType, path: str, platform: str, scheme: str, keyid: str = None): # pylint: disable=line-too-long
        self._provider = provider
        self._platform = platform
        self._path = path
        self._key = None
        self._scheme = scheme
        self._keyid = keyid

    async def load(self) -> None:
        """Invoke the underlying implementation to retrieve metadata
        for this specific key version.
        """
        assert self._key is None # nosec
        cls, params = await self._provider.load(self._path, scheme=self._scheme)
        self._key = cls(provider=self._provider, **params)
        self.get_secret = self._key.get_secret
        self.supports_signing_algorithm = self._key.supports_signing_algorithm
        self.wants_digest = self._key.wants_digest

    async def sign(self, data: bytes, algorithm: str, **kwargs) -> bytes:
        """Sign `data` using the given algorithm."""
        if not self.supports_signing_algorithm(algorithm):
            raise UnsupportedSigningAlgorithm(algorithm)
        if self.wants_digest() and not kwargs.get('prehashed'):
            data = bytes(Digest(algorithm, data))
        return await self._key.sign(data=data, algorithm=algorithm, **kwargs)

    async def verify(self,
        sig: bytes,
        data: bytes,
        algorithm: str,
        prehashed: bool = False,
        **kwargs
    ) -> bool:
        """Verifies that `sig` was created from `data` using this key."""
        if not self.supports_signing_algorithm(algorithm): # pragma: no cover
            raise UnsupportedSigningAlgorithm(algorithm)
        if self.wants_digest() and not prehashed:
            data = Digest(algorithm, data)
        return await self._key.verify(
            sig=sig,
            data=data,
            algorithm=algorithm,
            **kwargs
        )
