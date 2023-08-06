"""Declares :class:`HMACKey`."""
import hashlib

from .symmetrickey import SymmetricKey


DIGESTMOD = {
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
    'sha512': hashlib.sha512,
}


class HMACKey(SymmetricKey):
    __module__: str = 'unimatrix.ext.kms'

    async def get_secret(self) -> bytes:
        return bytes.fromhex(self.address)

    async def sign(self, data: bytes, algorithm: str) -> bytes:
        """Sign `message` using the configured cryptographic
        operations provider.
        """
        return await self.provider.sign_hmac(
            key=self,
            data=data,
            algorithm=algorithm
        )

    async def verify(self, sig: bytes, data: bytes, algorithm: str) -> bool:
        """Verifies that `sig` was created from `digest` using this key."""
        return await self.provider.verify_hmac(
            key=self,
            mac=sig,
            data=data,
            algorithm=algorithm
        )
