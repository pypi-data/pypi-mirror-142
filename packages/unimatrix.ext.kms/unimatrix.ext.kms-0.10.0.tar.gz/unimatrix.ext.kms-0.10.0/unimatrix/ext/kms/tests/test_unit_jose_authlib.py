# pylint: skip-file
import json
from authlib.jose import JsonWebSignature

from .josecompatibility import JOSECompatibility


class TestAuthlibCompatibility(JOSECompatibility):

    async def encode(self, key, algorithm, payload, headers=None, secret=None):
        jws = JsonWebSignature()
        headers = {**headers, 'alg': algorithm}
        secret = secret or await key.get_secret()
        return jws.serialize_compact(headers, json.dumps(payload), secret)
