# pylint: skip-file
from jose import jwt

from .josecompatibility import JOSECompatibility


class TestPythonJoseCompatibility(JOSECompatibility):

    def test_verify_ps256(self, keychain):
        pass

    def test_verify_ps384(self, keychain):
        pass

    def test_verify_ps512(self, keychain):
        pass

    async def encode(self, key, algorithm, payload, headers=None, secret=None):
        secret = secret or await key.get_secret()
        return jwt.encode(payload, secret, algorithm=algorithm, headers=headers)

