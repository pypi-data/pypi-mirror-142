"""Declares :class:`RSAPublicKey`."""
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa

from .rsamixin import RSAMixin
from .publickey import PublicKey


class RSAPublicKey(PublicKey, RSAMixin):
    __module__: str = 'unimatrix.ext.kms'

    @property
    def numbers(self) -> rsa.RSAPublicNumbers:
        return rsa.RSAPublicNumbers(
            n=self._n,
            e=self._e
        )

    @property
    def public(self) -> rsa.RSAPublicKey:
        return self.numbers.public_key()

    @classmethod
    def fromjwk(cls, jwk: dict):
        """Deserialize key material from a JSON Web Key (JWK)."""
        return cls.fromnumbers(jwk['n'], jwk['e'])

    @classmethod
    def fromnumbers(cls, n: int, e: int):
        """Deserialize key material from public numbers."""
        return cls(n.bit_length(), n, e)

    @classmethod
    def frompublic(cls, key: rsa.RSAPublicKey):
        """Instantiate a new :class:`PublicKey` using a public key
        implementation from the :mod:`cryptography` package.
        """
        numbers = key.public_numbers()
        return cls.fromnumbers(numbers.n, numbers.e)

    def __init__(self, size: int, n: int, e: int):
        self._size = size
        self._n = n
        self._e = e

    def get_identity_sequence(self) -> bytes:
        return int.to_bytes(self._n, (self._size // 8) + 1, 'big')\
            + int.to_bytes(self._e, 3, 'big')

    async def verify(self,
        sig: bytes,
        data: bytes,
        algorithm: str,
        padding: str = None,
        **kwargs
    ) -> bool:
        """Verifies that signature `sig` was created for `digest` using this
        key.
        """
        try:
            self.public.verify(
                signature=sig,
                data=bytes(data),
                padding=self.get_padding(
                    self._get_signing_algorithm(algorithm), padding
                ),
                algorithm=utils.Prehashed(
                    self._get_signing_algorithm(algorithm)
                )
            )
            return True
        except InvalidSignature:
            return False
