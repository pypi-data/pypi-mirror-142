"""Declares :class:`PublicKey`."""
from cryptography.hazmat.primitives.serialization import load_pem_public_key

from .asymmetrickey import AsymmetricKey


class PublicKey(AsymmetricKey):
    """Represents the public part of an asymmetric cryptographic key. The
    base :mod:`unimatrix.ext.kms.PublicKey` is an interface specification only;
    the implementation itself does not provide core functionality.
    """
    __module__: str = 'unimatrix.ext.kms'

    @classmethod
    def frompem(cls, pem: bytes): # pragma: no cover
        """Deserialize key material from a byte-sequence containing a
        PEM-encoded key.
        """
        return cls.frompublic(load_pem_public_key(pem))

    @classmethod
    def frompublic(cls, key: object):
        """Instantiate a new :class:`PublicKey` using a public key
        implementation from the :mod:`cryptography` package.
        """
        raise NotImplementedError

    def verify(self, sig: bytes, data: bytes, **kwargs):
        raise NotImplementedError
