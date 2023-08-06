"""Declares :class:`TrustStore`."""
from unimatrix.ext import cache

from .model import PublicKey


class TrustStore:
    """Provides an interface to (transiently) persist and lookup public keys
    from a shared cache.
    """
    __module__: str = 'unimatrix.ext.kms'

    #: The cache connection to use when persisting the keys.
    using: str = 'unimatrix.kms'

    def __init__(self, using: str = 'unimatrix.kms'):
        self.using = using

    async def add(self, key: PublicKey, ttl: int = None) -> None:
        """Adds a public key to the trust store.

        Args:
            key (:class:`~unimatrix.ext.kms.PublicKey`): the public key to add
                to the trust store.
            ttl (int): the number of seconds to retain the key. Defaults to
                ``86400`` seconds (one day) if omitted.

        Returns:
            None
        """
        await cache.set(key.keyid, str.encode(key.jwk), expires=ttl*1000)
