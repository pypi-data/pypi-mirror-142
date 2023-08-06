# pylint: skip-file
import base64
import binascii
import typing


def b64decode(buf: typing.Union[str, bytes]) -> bytes: # pragma: no cover
    if isinstance(buf, str):
        buf = buf.encode("ascii")
    rem = len(buf) % 4
    if rem > 0:
        buf += b"=" * (4 - rem)
    return base64.urlsafe_b64decode(buf)


def b64encode(buf: bytes) -> bytes: # pragma: no cover
    return base64.urlsafe_b64encode(buf).replace(b"=", b"")


def number_to_bytes(value: int, l: int) -> bytes:
    padded = str.encode("%0*x" % (2 * l, value), "ascii")
    return binascii.a2b_hex(padded)


def bytes_to_number(value: bytes) -> int:
    return int(binascii.b2a_hex(value), 16)
