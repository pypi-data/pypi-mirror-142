"""Declares :class:`RSAMixin`."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class RSAMixin:
    default_padding: str = 'PSS'

    def get_padding(self,
        algorithm: hashes.HashAlgorithm,
        scheme: str = None
    ) -> padding.AsymmetricPadding:
        """Return the padding scheme to use when signing/verifying."""
        scheme = scheme or self.default_padding
        if scheme in {'EMSA-PSS', 'PSS'}:
            instance = padding.PSS(
                mgf=padding.MGF1(algorithm),
                salt_length=algorithm.digest_size
            )
        elif scheme in {'EMSA-PKCS1-v1_5', 'PKCS1v15'}:
            instance = padding.PKCS1v15()
        else: # pragma: no cover
            raise ValueError(f"Unsupported scheme: {scheme}")
        return instance

    def normalize_signature(self, sig: bytes) -> bytes:
        return sig
