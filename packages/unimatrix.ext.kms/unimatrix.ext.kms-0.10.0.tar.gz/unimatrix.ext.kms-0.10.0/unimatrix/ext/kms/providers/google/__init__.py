"""Provides integration with Google Cloud KMS."""
from google.cloud.kms import KeyManagementServiceAsyncClient

from unimatrix.ext import kms
from .cryptokeyaddress import CryptoKeyAddress
from .keyrepository import KeyRepository


__all__ = [
    'load'
]

ALGORITHM_CLASSES = {
    'HMAC_SHA256': kms.HMACKey,
    'EC_SIGN_P256_SHA256': kms.EllipticCurvePrivateKey,
    'EC_SIGN_P384_SHA384': kms.EllipticCurvePrivateKey,
    'EC_SIGN_SECP256K1_SHA256': kms.EllipticCurvePrivateKey,
    'RSA_SIGN_PSS_2048_SHA256': kms.RSAPrivateKey,
    'RSA_SIGN_PSS_3072_SHA256': kms.RSAPrivateKey,
    'RSA_SIGN_PSS_4096_SHA256': kms.RSAPrivateKey,
    'RSA_SIGN_PSS_4096_SHA512': kms.RSAPrivateKey,
    'RSA_SIGN_PKCS1_2048_SHA256': kms.RSAPrivateKey,
    'RSA_SIGN_PKCS1_3072_SHA256': kms.RSAPrivateKey,
    'RSA_SIGN_PKCS1_4096_SHA256': kms.RSAPrivateKey,
    'RSA_SIGN_PKCS1_4096_SHA512': kms.RSAPrivateKey,
}
repo = KeyRepository()


async def expand_path(address: str):
    return await repo.get_versions(CryptoKeyAddress.parse(address))


async def load(address: CryptoKeyAddress, *args, **kwargs):
    algorithm, params, public = await repo.get(address)
    cls = ALGORITHM_CLASSES[algorithm]
    if public is not None:
        params['public'] = cls.public_key_class.frompem(public)
    return cls, {**params, 'address': address}


async def sign(
    key: kms.PrivateKey,
    address: CryptoKeyAddress,
    data: bytes,
    context: dict,
    **kwargs
) -> bytes:
    async with KeyManagementServiceAsyncClient() as client:
        response = await client.asymmetric_sign(
            request={
                'name': address.as_version(client),
                'digest': {context['algorithm']: data}
            },
            timeout=10
        )
    return key.normalize_signature(response.signature)


async def sign_hmac(key: kms.HMACKey, data: bytes, **kwargs) -> bytes:
    """Create a Hash-based Message Authentication Code (HMAC) using
    the given key.
    """
    async with KeyManagementServiceAsyncClient() as client:
        response = await client.mac_sign(
            request={
                'name': key.address.as_version(client),
                'data': data
            }
        )
    return response.mac


async def verify_hmac(
    key: kms.HMACKey,
    mac: bytes,
    data: bytes,
    algorithm: str,
    **kwargs
) -> bool:
    """Verify that the Hash-based Message Authentication Code (HMAC) `mac` is
    valid for `digest`.
    """
    async with KeyManagementServiceAsyncClient() as client:
        response = await client.mac_verify(
            request={
                'name': key.address.as_version(client),
                'data': data,
                'mac': mac
            }
        )
    return response.success
