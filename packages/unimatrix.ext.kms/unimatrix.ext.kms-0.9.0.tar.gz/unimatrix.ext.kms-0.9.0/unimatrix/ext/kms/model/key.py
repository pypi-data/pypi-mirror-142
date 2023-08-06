"""Declares :class:`Key`."""
import functools
import hashlib
from types import ModuleType


class Key:
    """The base class for all cryptographic key implementations."""
    __module__: str = 'unimatrix.ext.kms'

    @classmethod
    def fromfile(cls, filepath: str):
        """Deserialize key material from a file located on the local
        filesystem.
        """
        raise NotImplementedError

    @classmethod
    def fromjwk(cls, jwk: dict):
        """Deserialize key material from a JSON Web Key (JWK)."""
        raise NotImplementedError

    @classmethod
    def frompem(cls, pem: bytes):
        """Deserialize key material from a byte-sequence containing a
        PEM-encoded key.
        """
        raise NotImplementedError

    @property
    def address(self) -> str:
        """Return the qualified name of the key."""
        return self._address

    @functools.cached_property
    def keyid(self) -> str:
        """Return as string that uniquely identifies the key based on
        implementation-specific variable (e.g. ``x`` and ``y`` for elliptic
        curve keypairs, ``n`` and ``e`` for RSA keypairs).
        """
        return hashlib.md5(self.get_identity_sequence()).hexdigest() # nosec

    @property
    def provider(self) -> ModuleType:
        """"Return the cryptopgraphic operation provider that is
        configured for this key.
        """
        return self._provider

    def __init__(self, provider: ModuleType, address: str, capabilities: set):
        self._provider = provider
        self._address = address
        self._capabilities = capabilities

    def as_bytes(self) -> bytes:
        """Represent the key as a byte-sequence."""
        raise NotImplementedError

    def get_identity_sequence(self) -> bytes:
        """Return a sequence of bytes that uniquely identifies the key."""
        raise NotImplementedError

    def supports_signing_algorithm(self, algorithm: str) -> bool:
        """Return a boolean indicating if the key can sign using the given
        algorithm `algorithm`.
        """
        raise NotImplementedError

    def wants_digest(self) -> bool:
        """Return a boolean indicating if the key requires a message digest
        for a signing or verification operation. If the key does not support
        digital signatures, :meth:`wants_digest` always returns ``False``.
        """
        return False
