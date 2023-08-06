"""Declares :class:`EllipticCurvePrivateKey`."""
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

from .ellipticcurvepublickey import EllipticCurvePublicKey
from .ellipticcurvemixin import EllipticCurveMixin
from .privatekey import PrivateKey


class EllipticCurvePrivateKey(PrivateKey, EllipticCurveMixin):
    """Represents an elliptic curve private key with the curve specified
    to the constructor.
    """
    __module__: str = 'unimatrix.ext.kms'
    public_key_class: type = EllipticCurvePublicKey

    def __init__(self, curve: str, **kwargs):
        super().__init__(**kwargs)
        self._curve = curve

    async def sign(self, data: bytes, algorithm: str, **kwargs) -> bytes:
        return await self.provider.sign(
            key=self,
            address=self.address,
            data=data,
            signature_algorithm=ec.ECDSA(
                utils.Prehashed(self._get_signing_algorithm(algorithm))
            ),
            context={'algorithm': algorithm}
        )
