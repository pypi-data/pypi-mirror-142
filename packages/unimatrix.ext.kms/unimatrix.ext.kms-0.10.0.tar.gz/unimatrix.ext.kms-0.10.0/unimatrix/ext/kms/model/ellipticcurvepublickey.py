"""Declares :class:`EllipticCurvePublicKey`."""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

from .ec import get_curve_impl
from .ec import normalize_curve
from .ellipticcurvemixin import EllipticCurveMixin
from .publickey import PublicKey


class EllipticCurvePublicKey(PublicKey, EllipticCurveMixin):
    """Represents an elliptic curve public key."""
    __module__: str = 'unimatrix.ext.kms'

    @property
    def numbers(self) -> ec.EllipticCurvePublicNumbers:
        return ec.EllipticCurvePublicNumbers(
            curve=get_curve_impl(self._curve),
            x=self._x,
            y=self._y
        )

    @property
    def public(self) -> ec.EllipticCurvePublicKey:
        return self.numbers.public_key()

    @classmethod
    def frompublic(cls, key: ec.EllipticCurvePublicKey):
        """Instantiate a new :class:`PublicKey` using a public key
        implementation from the :mod:`cryptography` package.
        """
        numbers = key.public_numbers()
        return cls(
            curve=normalize_curve(key.curve.name),
            x=numbers.x,
            y=numbers.y
        )

    def __init__(self, curve: str, x: int, y: int):
        self._curve = curve
        self._x = x
        self._y = y

    async def verify(self, sig: bytes, data: bytes, algorithm: str, **kwargs) -> bool:
        try:
            self.public.verify(
                signature=self.denormalize_signature(sig),
                data=bytes(data),
                signature_algorithm=ec.ECDSA(
                    utils.Prehashed(self._get_signing_algorithm(algorithm))
                )
            )
            return True
        except InvalidSignature:
            return False

    def get_identity_sequence(self) -> bytes:
        size = self.numbers.curve.key_size // 8
        if size == 65:  # TODO !!!
            size = 128
        return int.to_bytes(self._x, size, 'big')\
            + int.to_bytes(self._y, size, 'big')
