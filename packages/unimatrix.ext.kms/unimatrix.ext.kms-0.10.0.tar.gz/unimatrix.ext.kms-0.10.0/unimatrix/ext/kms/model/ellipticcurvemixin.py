"""Declares :class:`EllipticCurveMixin`."""
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurve
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature

from ..utils import bytes_to_number
from ..utils import number_to_bytes


CURVE_CLASSES = {
    'P-256': ec.SECP256R1,
    'P-256K': ec.SECP256K1,
    'P-384': ec.SECP384R1,
    'P-521': ec.SECP521R1
}


class EllipticCurveMixin:

    @property
    def curve(self) -> EllipticCurve:
        return CURVE_CLASSES[self._curve]

    def normalize_signature(self, sig: bytes) -> bytes:
        num_bits = self.curve.key_size
        num_bytes = (num_bits + 7) // 8
        r, s = decode_dss_signature(sig)
        return number_to_bytes(r, num_bytes) + number_to_bytes(s, num_bytes)

    def denormalize_signature(self, sig: bytes) -> bytes:
        num_bits = self.curve.key_size
        num_bytes = (num_bits + 7) // 8
        if len(sig) != 2 * num_bytes: # pragma: no cover
            raise ValueError("Invalid signature")
        r = bytes_to_number(sig[:num_bytes])
        s = bytes_to_number(sig[num_bytes:])
        return encode_dss_signature(r, s)
