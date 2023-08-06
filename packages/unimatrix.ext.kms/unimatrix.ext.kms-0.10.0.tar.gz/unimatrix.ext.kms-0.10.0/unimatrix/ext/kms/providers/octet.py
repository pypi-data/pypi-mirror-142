"""A provider implementation that used in-memory octet sequences as signing
and encryption keys.
"""
import hmac

from unimatrix.ext.kms.model import HMACKey


async def load(address: str, scheme: str, platform: str = None):
    """Discover the key type and parameters from the given address,
    scheme and parameters.
    """
    capabilities = ['sig']
    _, fmt = str.split(scheme, '+')
    if fmt == 'aes': # pragma: no cover
        raise NotImplementedError
    return HMACKey, {
        'address': address,
        'capabilities': capabilities,
        'secret': bytes.fromhex(address),
        'sigalg': {'sha256', 'sha384', 'sha512'}
    }


async def sign_hmac(key: HMACKey, data: bytes, algorithm: str) -> bytes:
    """Create a Hash-based Message Authentication Code (HMAC) using
    the given key.
    """
    return hmac.digest(await key.get_secret(), data, algorithm)


async def verify_hmac(
    key: HMACKey,
    mac: bytes,
    data: bytes,
    algorithm: str,
) -> bool:
    """Verify that the Hash-based Message Authentication Code (HMAC) `mac` is
    valid for `digest`.
    """
    return hmac.compare_digest(mac, await sign_hmac(key, data, algorithm))
