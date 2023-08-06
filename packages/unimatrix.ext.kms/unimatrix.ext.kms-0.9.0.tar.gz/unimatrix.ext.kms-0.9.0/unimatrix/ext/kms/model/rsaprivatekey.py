"""Declares :class:`RSAPrivateKey`."""
import typing

from cryptography.hazmat.primitives.asymmetric import utils

from .privatekey import PrivateKey
from .rsamixin import RSAMixin
from .rsapublickey import RSAPublicKey


class RSAPrivateKey(PrivateKey, RSAMixin):
    """Represents an RSA private key with the key size specified
    to the constructor.
    """
    __module__: str = 'unimatrix.ext.kms'
    public_key_class: type = RSAPublicKey

    def __init__(self, size: typing.Literal[2048, 4096, 8192], **kwargs):
        super().__init__(**kwargs)
        self._size = size

    async def sign(self,
        data: bytes,
        algorithm: str,
        padding: typing.Union['PSS', 'PKCS1v15'] = None,
        **kwargs
    ) -> bytes:
        return await self.provider.sign(
            key=self,
            address=self.address,
            data=data,
            padding=self.get_padding(
                self._get_signing_algorithm(algorithm), padding
            ),
            algorithm=utils.Prehashed(self._get_signing_algorithm(algorithm)),
            context={'algorithm': algorithm}
        )
