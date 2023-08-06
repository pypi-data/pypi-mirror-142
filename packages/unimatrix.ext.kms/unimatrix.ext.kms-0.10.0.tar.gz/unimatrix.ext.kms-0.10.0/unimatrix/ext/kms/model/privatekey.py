"""Declares :class:`PrivateKey`."""
from .asymmetrickey import AsymmetricKey
from .publickey import PublicKey


class PrivateKey(AsymmetricKey):
    """The base class for all private key implementations."""
    __module__: str = 'unimatrix.ext.kms'

    @property
    def public(self) -> PublicKey:
        """Return the :class:`PublicKey` for this private key."""
        return self._public

    @property
    def public_key_class(self) -> type:
        raise NotImplementedError

    def __init__(self, public: PublicKey, sigalg: set = None, **kwargs):
        super().__init__(**kwargs)
        self._public = public
        self._sigalg = sigalg or set()

    def supports_signing_algorithm(self, algorithm: str) -> bool:
        """Return a boolean indicating if the key can sign using the given
        algorithm `algorithm`.
        """
        return algorithm in self._sigalg

    def verify(self, sig: bytes, data: bytes, *args, **kwargs) -> bool:
        """Verifies that `sig` was created from `digest` using this key."""
        return self.public.verify(sig, data, *args, **kwargs)

    async def sign(self, data: bytes, **kwargs) -> bytes:
        """Sign `message` using the configured cryptographic
        operations provider.
        """
        raise NotImplementedError

    def get_identity_sequence(self) -> bytes:
        return self._public.get_identity_sequence()
