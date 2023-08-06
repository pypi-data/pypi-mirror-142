"""Declares the module interface for cryptographic operations providers. This
specific module implements PEM-encoded keys loaded from the local disk.
"""
import typing

import aiofiles
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from unimatrix.ext.kms.model import EllipticCurvePrivateKey
from unimatrix.ext.kms.model import EllipticCurvePublicKey
from unimatrix.ext.kms.model import PrivateKey
from unimatrix.ext.kms.model import RSAPrivateKey
from unimatrix.ext.kms.model import RSAPublicKey
from unimatrix.ext.kms.model.ec import CURVE_MAPPING as CURVES


class PEMMixin:

    async def get_secret(self) -> bytes:
        return await self.get_pem()

    async def get_pem(self) -> bytes:
        async with aiofiles.open(self.address, 'rb') as f:
            return await f.read()


async def _read(address):
    async with aiofiles.open(address, 'rb') as f:
        pem = await f.read()
        return load_pem_private_key(pem, None)


async def load(address: str, **kwargs) -> typing.Tuple[str, dict]:
    """Inspect metadata and return a tuple containing a concrete implementation
    of :class:`~unimatrix.ext.kms.model.Key` and a :class:`Metadata` instance.
    """
    impl = await _read(address)
    if isinstance(impl, ec.EllipticCurvePrivateKey):
        cls = type(
            'EllipticCurvePrivateKey',
            (EllipticCurvePrivateKey, PEMMixin),
            {}
        )
        kwargs = {
            'curve': CURVES[impl.curve.name],
            'public': EllipticCurvePublicKey.frompublic(impl.public_key())
        }
    elif isinstance(impl, rsa.RSAPrivateKey):
        cls = type('RSAPrivateKey', (RSAPrivateKey, PEMMixin), {})
        kwargs = {
            'public': RSAPublicKey.frompublic(impl.public_key()),
            'size': impl.key_size
        }
    else:
        raise NotImplementedError(f"Unsupported key in {address}")
    kwargs.update({
        'address': address,
        'sigalg': {'sha256', 'sha384', 'sha512'},
        'capabilities': {'enc', 'sig'},
    })
    return cls, kwargs


async def sign(
    key: PrivateKey,
    address: str,
    data: bytes,
    context: dict = None,
    **kwargs
) -> bytes:
    """Sign `digest` using the specified key."""
    impl = await _read(address)
    return key.normalize_signature(impl.sign(data, **kwargs))
