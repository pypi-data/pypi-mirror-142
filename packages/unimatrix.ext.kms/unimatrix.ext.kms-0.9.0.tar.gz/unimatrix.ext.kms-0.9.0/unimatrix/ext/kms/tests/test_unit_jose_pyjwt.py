# pylint: skip-file
import jwt

from .josecompatibility import JOSECompatibility


class TestPyJWTCompatibility(JOSECompatibility):

    async def encode(self, key, algorithm, payload, headers=None, secret=None):
        secret = secret or await key.get_secret()
        return jwt.encode(payload, secret, algorithm=algorithm, headers=headers)
