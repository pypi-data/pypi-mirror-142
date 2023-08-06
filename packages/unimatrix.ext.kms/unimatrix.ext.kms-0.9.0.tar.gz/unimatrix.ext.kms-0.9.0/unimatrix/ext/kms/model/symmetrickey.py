"""Declares :class:`SymmetricKey`."""
from .key import Key


class SymmetricKey(Key):
    __module__: str = 'unimatrix.ext.kms'

    @property
    def secret(self) -> bytes:
        """Return the secret of this key."""
        return self._secret

    def __init__(self, secret: str = None, sigalg: set = None, **kwargs):
        super().__init__(**kwargs)
        self._secret = secret
        self._sigalg = sigalg or set()

    def supports_signing_algorithm(self, algorithm: str) -> bool:
        """Return a boolean indicating if the key can sign using the given
        algorithm `algorithm`.
        """
        return algorithm in self._sigalg

    async def sign(self, data: bytes, **kwargs) -> bytes:
        """Sign `message` using the configured cryptographic
        operations provider.
        """
        raise NotImplementedError

    async def verify(self, sig: bytes, data: bytes, *args, **kwargs) -> bool:
        """Verifies that `sig` was created from `data` using this key."""
        raise NotImplementedError
