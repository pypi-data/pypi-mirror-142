# pylint: skip-file
import asyncio
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from unimatrix.ext import kms


os.environ['SECRET_AES128_KEY'] = bytes.hex(os.urandom(16))
os.environ['SECRET_AES192_KEY'] = bytes.hex(os.urandom(24))
os.environ['SECRET_AES256_KEY'] = bytes.hex(os.urandom(32))
os.environ['SECRET_HMAC_KEY'] = bytes.hex(os.urandom(16))


async def main():
    await kms.register('rsa', 'file+pem:pki/rsa.key')
    await kms.register('ec', [
        'file+pem:pki/p256.key',
        'file+pem:pki/p256k.key',
        'file+pem:pki/rsa.key',
    ])

    # Create and verify as signature using an elliptic curve key.
    key = kms.get('ec')
    sig = await kms.sign(b'Hello world!', using='ec', algorithm='sha256')
    assert key.verify(sig, b'Hello world!', algorithm='sha256')

    # Create and verify a signature using a RSA key.
    key = kms.get('rsa')
    sig = await kms.sign(b'Hello world!', using='rsa', algorithm='sha256')
    assert key.verify(sig, b'Hello world!', algorithm='sha256')
    assert not key.verify(sig, b'Invalid data', algorithm='sha256')


if __name__ == '__main__':
    asyncio.run(main())
