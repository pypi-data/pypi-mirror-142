# pylint: skip-file
import hashlib
import typing

from ..model import PrivateKey
from ..model import PublicKey


_PRESETS = {}
register = _PRESETS.__setitem__
get = _PRESETS.__getitem__


class BasePreset:
    algorithm: str
    padding: str = None
    needs_digest: bool = True

    @staticmethod
    def get_digest(algorithm: str, data: bytes) -> bytes:
        if algorithm not in {'sha256', 'sha384', 'sha512'}:
            raise TypeError("Invalid algorithm.")
        return getattr(hashlib, algorithm)(data).digest()

    def get_signing_kwargs(self) -> dict:
        kwargs = {
            'algorithm': self.algorithm,
            'prehashed': True
        }
        if self.padding is not None:
            kwargs['padding'] = self.padding
        return kwargs

    async def sign(self, key: PrivateKey, data: bytes) -> bytes:
        return await key.sign(key, data, **self.get_signing_kwargs())

    async def verify(self,
        key: typing.Union[PublicKey, PrivateKey],
        signature: bytes,
        data: bytes,
        prehashed: bool = True
    ) -> bool:
        """Verify that `signature` was created from `data` using `key`."""
        if not prehashed and self.needs_digest:
            data = self.get_digest(self.algorithm, data)
        return await key.verify(signature, data, **self.get_signing_kwargs())


class HMACSHA256(BasePreset):
    algorithm: str = 'sha256'
    needs_digest: bool = False


class HMACSHA384(BasePreset):
    algorithm: str = 'sha384'
    needs_digest: bool = False


class HMACSHA512(BasePreset):
    algorithm: str = 'sha512'
    needs_digest: bool = False


class RSAPKCS1v15withSHA256(BasePreset):
    algorithm: str = 'sha256'
    padding: str = 'PKCS1v15'


class RSAPKCS1v15withSHA384(BasePreset):
    algorithm: str = 'sha384'
    padding: str = 'PKCS1v15'


class RSAPKCS1v15withSHA512(BasePreset):
    algorithm: str = 'sha512'
    padding: str = 'PKCS1v15'


class RSAPSSwithSHA256(BasePreset):
    algorithm: str = 'sha256'
    padding: str = 'PSS'


class RSAPSSwithSHA384(BasePreset):
    algorithm: str = 'sha384'
    padding: str = 'PSS'


class RSAPSSwithSHA512(BasePreset):
    algorithm: str = 'sha512'
    padding: str = 'PSS'


class P256withSHA256(BasePreset):
    algorithm: str = 'sha256'
    curve: str = 'P-256'


class P384withSHA384(BasePreset):
    algorithm: str = 'sha384'
    curve: str = 'P-384'


class P521withSHA512(BasePreset):
    algorithm: str = 'sha512'
    curve: str = 'P-521'


class P256KwithSHA256(BasePreset):
    algorithm: str = 'sha256'
    curve: str = 'P-256K'



register('HS256', HMACSHA256())
register('HS384', HMACSHA384())
register('HS512', HMACSHA512())
register('RS256', RSAPKCS1v15withSHA256())
register('RS384', RSAPKCS1v15withSHA384())
register('RS512', RSAPKCS1v15withSHA512())
register('PS256', RSAPSSwithSHA256())
register('PS384', RSAPSSwithSHA384())
register('PS512', RSAPSSwithSHA512())
register('ES256', P256withSHA256())
register('ES384', P384withSHA384())
register('ES512', P521withSHA512())
register('ES256K', P256KwithSHA256())
