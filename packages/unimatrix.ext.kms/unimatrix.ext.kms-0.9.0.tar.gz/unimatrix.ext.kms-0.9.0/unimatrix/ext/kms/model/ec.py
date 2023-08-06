# pylint: disable=line-too-long
"""Declares constants and helper functions related to Elliptic
Curve (EC) cryptography.
"""
from cryptography.hazmat.primitives.asymmetric import ec


CURVES = ('P-256', 'P-256K')

CURVE_CLASSES = {
    'P-256': ec.SECP256R1,
    'P-256K': ec.SECP256K1,
    'P-384': ec.SECP384R1,
    'P-521': ec.SECP521R1
}

CURVE_MAPPING = {
    'secp256r1': "P-256",
    'secp256k1': "P-256K",
    'secp384r1': "P-384",
    'secp521r1': "P-521",
}


def get_curve_impl(curve: str) -> ec.EllipticCurve:
    """Get the :class:`cryptography.hazmat.primitives.asymmetric.ec.EllipticCurve`
    corresponding to named curve `curve`.
    """
    return CURVE_CLASSES[curve]()


def normalize_curve(curve: str) -> str:
    """Normalize the name of an elliptic curve."""
    return CURVE_MAPPING[curve]
