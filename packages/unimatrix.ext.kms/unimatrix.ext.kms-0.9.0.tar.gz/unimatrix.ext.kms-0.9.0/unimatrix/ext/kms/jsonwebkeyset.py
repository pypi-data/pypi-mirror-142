"""Declares :class:`JSONWebKeySet`."""
import collections
import json
import typing

from .utils import b64decode
from .jsonwebkey import JSONWebKey


INT_MEMBERS = {'e', 'n', 'x', 'y'}


class JSONWebKeySet:
    """Contains a JSON Web Key Set (JWKS). The current imlementation of
    :class:`JSONWebKeySet` only supports public keys for RSA and Elliptic
    Curve (EC). Unknown keys types are silently ignored.
    """
    __module__: str = 'unimatrix.ext.kms'

    @classmethod
    def fromjson(cls, serialized: typing.Union[bytes, str]):
        """Instantiate a :class:`JSONWebKeySet` from serialized JSON."""
        if isinstance(serialized, bytes):
            serialized = bytes.decode(serialized, "utf-8")
        return cls.fromdict(json.loads(serialized))

    @classmethod
    def fromdict(cls, jwks: dict):
        """Instantiate a :class:`JSONWebKeySet` from a dictionary."""
        keys = []
        for jwk in jwks.get('keys'):
            for k in jwk:
                if k not in INT_MEMBERS:
                    continue
                jwk[k] = int.from_bytes(b64decode(jwk[k]), 'big')
            keys.append(JSONWebKey.fromjwk(jwk))
        return cls(keys)

    def __init__(self, keys: list = None):
        self._keys = keys or []
        self._index = collections.OrderedDict(
            [(x.kid, x) for x in self._keys if x.kid]
        )

    async def verify(self,
        signature: bytes,
        payload: bytes,
        algorithm: str = None,
        using: str = None
    ) -> bool:
        """Verify `signature` using the JSON Web Key Set. The `kid`
        parameter specifies the key to use; if `kid` is ``None``, then
        try all keys.
        """
        kid = using
        is_valid = False
        if kid is not None:
            if kid in self._index:
                key = self._index[kid]
                is_valid = await key.verify(signature, payload, preset=algorithm)
        else:
            for key in self._keys:
                is_valid = await key.verify(signature, payload, preset=algorithm)
                if is_valid:
                    break
        return is_valid

    def __add__(self, jwks):
        return JSONWebKeySet(self._keys + jwks._keys)

    def __radd__(self, jwks):
        return JSONWebKeySet(jwks._keys + self._keys)

    def __iter__(self):
        return iter(self._index.values())

    def __len__(self) -> int:
        return len(self._keys)
