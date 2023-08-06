"""Declares :class:`AsymmetricKey`."""
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hashes import SHA384
from cryptography.hazmat.primitives.hashes import SHA512

from .key import Key


HASH_MAPPING = {
    'sha256': SHA256,
    'sha384': SHA384,
    'sha512': SHA512,
}


class AsymmetricKey(Key):
    """Specifies an interface for asymmetric keypairs."""
    __module__: str = 'unimatrix.ext.kms'

    def _get_signing_algorithm(self, algorithm: str):
        return HASH_MAPPING[algorithm]()

    def wants_digest(self) -> bool:
        """Return a boolean indicating if the key requires a message digest
        for a signing or verification operation.
        """
        return True

