"""Declares :class:`HMACKey`."""
from unimatrix.ext import kms


class HMACKey(kms.SymmetricKey):
    __module__: str = 'unimatrix.ext.kms.providers.google'
