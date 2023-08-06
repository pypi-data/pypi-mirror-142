"""Declares :class:`JSONWebKey`."""
import typing

from .model import Key
from .model import EllipticCurvePublicKey
from .model import RSAPublicKey
from .presets import get as preset


class JSONWebKey:
    __module__: str = 'unimatrix.ext.kms'
    _key_classes: dict = {
        "EC": EllipticCurvePublicKey,
        "RSA": RSAPublicKey
    }

    @property
    def kid(self) -> typing.Union[str, None]:
        return self._kid

    @classmethod
    def fromjwk(cls, jwk: dict):
        return cls(cls._key_classes[ jwk['kty'] ].fromjwk(jwk), **jwk)

    def __init__(self,
        key: Key,
        kid: str = None,
        use: str = None,
        alg: str = None,
        **kwargs
    ):
        self._key = key
        self._kid = kid
        self._use = use
        self._alg = alg
        self._preset = preset(alg) if alg else None

    async def verify(self,
        signature: bytes,
        payload: bytes,
        preset: str = None
    ) -> bool:
        """Verify the signature using the JSON Web Key (JWK)."""
        if not self._preset and preset is None:
            raise NotImplementedError
        if self._alg and preset not in {self._alg, None}:
            return False
        preset = self._preset
        return await preset.verify(
            key=self._key,
            signature=signature,
            data=payload,
            prehashed=False
        )
