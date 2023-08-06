"""Declares :class:`Signature`."""
import typing

from .joseheader import JOSEHeader
from .jsonwebkeyset import JSONWebKeySet
from .keychain import Keychain
from .utils import b64decode


class Signature:
    """Represents the digital signature of a JSON Web Signature (JWS)."""
    __module__: str = 'unimatrix.ext.kms'

    @property
    def algorithm(self) -> str:
        return self._header.algorithm

    @property
    def kid(self) -> str:
        return self._header.kid

    def __init__(self,
        header: JOSEHeader,
        protected: str,
        signature: str,
        claims: dict = None
    ):
        """The :class:`Signature` class may be used with both JWS Compact
        Serialization as well as JWS JSON Serialization.

        Args:
            header (:class:`JOSEHeader`): the header that was parsed from the
                JSON Web Token (JWT).
            protected (str): the original, URL-encoded protected header.
            signature (str): the signature over protected and payload.
            claims (dict): optional unprotected claims.
        """
        self._header = header
        self._protected = protected
        self._signature = b64decode(signature)
        self._claims = claims

    async def verify(self,
        verifier: typing.Union[Keychain, JSONWebKeySet],
        payload: bytes
    ) -> bool:
        return await verifier.verify(
            signature=self._signature,
            payload=payload,
            algorithm=self.algorithm,
            using=self.kid
        )
