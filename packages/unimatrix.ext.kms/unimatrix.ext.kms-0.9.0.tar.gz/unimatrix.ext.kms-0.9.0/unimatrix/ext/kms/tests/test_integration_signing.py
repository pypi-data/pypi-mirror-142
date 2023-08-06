# pylint: skip-file
import os

import pytest

from ..const import TEST_HMAC_KEY
from .basesigning import BaseSigning

# These signing tests should cover all algorithms mentioned in the
# JSON Web Algorithm (RFC 7518) specification:
#
#   +--------------+-------------------------------+--------------------+
#   | "alg" Param  | Digital Signature or MAC      | Implementation     |
#   | Value        | Algorithm                     | Requirements       |
#   +--------------+-------------------------------+--------------------+
#   | HS256        | HMAC using SHA-256            | Required           |
#   | HS384        | HMAC using SHA-384            | Optional           |
#   | HS512        | HMAC using SHA-512            | Optional           |
#   | RS256        | RSASSA-PKCS1-v1_5 using       | Recommended        |
#   |              | SHA-256                       |                    |
#   | RS384        | RSASSA-PKCS1-v1_5 using       | Optional           |
#   |              | SHA-384                       |                    |
#   | RS512        | RSASSA-PKCS1-v1_5 using       | Optional           |
#   |              | SHA-512                       |                    |
#   | ES256        | ECDSA using P-256 and SHA-256 | Recommended+       |
#   | ES384        | ECDSA using P-384 and SHA-384 | Optional           |
#   | ES512        | ECDSA using P-521 and SHA-512 | Optional           |
#   | PS256        | RSASSA-PSS using SHA-256 and  | Optional           |
#   |              | MGF1 with SHA-256             |                    |
#   | PS384        | RSASSA-PSS using SHA-384 and  | Optional           |
#   |              | MGF1 with SHA-384             |                    |
#   | PS512        | RSASSA-PSS using SHA-512 and  | Optional           |
#   |              | MGF1 with SHA-512             |                    |
#   | none         | No digital signature or MAC   | Optional           |
#   |              | performed                     |                    |
#   +--------------+-------------------------------+--------------------+


class TestP256SHA256(BaseSigning):
    address = 'file+pem:pki/p256.key'
    algorithm = 'sha256'


class TestP256SHA384(BaseSigning):
    address = 'file+pem:pki/p256.key'
    algorithm = 'sha384'


class TestP256SHA512(BaseSigning):
    address = 'file+pem:pki/p256.key'
    algorithm = 'sha512'


class TestP384SHA256(BaseSigning):
    address = 'file+pem:pki/p384.key'
    algorithm = 'sha256'


class TestP384SHA384(BaseSigning):
    address = 'file+pem:pki/p384.key'
    algorithm = 'sha384'


class TestP384SHA512(BaseSigning):
    address = 'file+pem:pki/p384.key'
    algorithm = 'sha512'


class TestP521SHA256(BaseSigning):
    address = 'file+pem:pki/p521.key'
    algorithm = 'sha256'


class TestP521SHA384(BaseSigning):
    address = 'file+pem:pki/p521.key'
    algorithm = 'sha384'


class TestP521SHA512(BaseSigning):
    address = 'file+pem:pki/p521.key'
    algorithm = 'sha512'


class TestP256KSHA256(BaseSigning):
    address = 'file+pem:pki/p256k.key'
    algorithm = 'sha256'


class TestP256KSHA384(BaseSigning):
    address = 'file+pem:pki/p256k.key'
    algorithm = 'sha384'


class TestP256KSHA512(BaseSigning):
    address = 'file+pem:pki/p256k.key'
    algorithm = 'sha512'


class TestRSAPSSSHA256(BaseSigning):
    address = 'file+pem:pki/rsa.key'
    algorithm = 'sha256'
    padding = 'PSS'

    def get_signing_params(self):
        return {'padding': self.padding}


class TestRSAPSSSHA384(TestP256SHA256):
    algorithm = 'sha384'


class TestRSAPSSSHA512(TestRSAPSSSHA256):
    algorithm = 'sha512'


class TestRSAPKCS1v15SHA256(TestRSAPSSSHA256):
    algorithm = 'sha256'
    padding = 'PKCS1v15'


class TestRSAPKCS1v15SHA384(TestRSAPSSSHA256):
    algorithm = 'sha384'
    padding = 'PKCS1v15'


class TestRSAPKCS1v15SHA512(TestRSAPSSSHA256):
    algorithm = 'sha512'
    padding = 'PKCS1v15'


class TestHMACSHA256(BaseSigning):
    address = f'literal+hmac:{TEST_HMAC_KEY}?keyid=hmac'
    algorithm = 'sha256'
    has_identity = False


class TestHMACSHA384(BaseSigning):
    address = f'literal+hmac:{TEST_HMAC_KEY}?keyid=hmac'
    algorithm = 'sha384'
    has_identity = False


class TestHMACSHA512(BaseSigning):
    address = f'literal+hmac:{TEST_HMAC_KEY}?keyid=hmac'
    algorithm = 'sha512'
    has_identity = False


#-------------------------------------------------------------------------------
#
#   GOOGLE CLOUD KMS TESTS
#
#-------------------------------------------------------------------------------
onlygoogle = pytest.mark.skipif(
    not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
    reason="Google Cloud not authenticated."
)

@onlygoogle
class TestGoogleP256SHA256(BaseSigning):
    address = "cloud+google:unimatrixdev/europe-west4/local/ec_sign_p256_sha256"
    algorithm = 'sha256'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleP256KSHA256(BaseSigning):
    address = "cloud+google:unimatrixdev/europe-west4/local/ec_sign_secp256k1_sha256"
    algorithm = 'sha256'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleP384SHA384(BaseSigning):
    address = "cloud+google:unimatrixdev/europe-west4/local/ec_sign_p384_sha384"
    algorithm = 'sha384'
    unsupported_signing_algorithms = {'sha256', 'sha512'}


@onlygoogle
class TestGoogleRSA2048PSSSHA256(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pss_2048_sha256"
    algorithm = 'sha256'
    padding = 'PSS'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleRSA3072PSSSHA256(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pss_3072_sha256"
    algorithm = 'sha256'
    padding = 'PSS'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleRSA4096PSSSHA256(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pss_4096_sha256"
    algorithm = 'sha256'
    padding = 'PSS'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleRSA4096PSSSHA512(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pss_4096_sha512"
    algorithm = 'sha512'
    padding = 'PSS'
    unsupported_signing_algorithms = {'sha256', 'sha384'}


@onlygoogle
class TestGoogleRSA2048PKCS1v15SHA256(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pkcs1_2048_sha256"
    algorithm = 'sha256'
    padding = 'PKCS1v15'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleRSA3072PKCS1v15SHA256(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pkcs1_3072_sha256"
    algorithm = 'sha256'
    padding = 'PKCS1v15'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleRSA4096PKCS1v15SHA256(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pkcs1_4096_sha256"
    algorithm = 'sha256'
    padding = 'PKCS1v15'
    unsupported_signing_algorithms = {'sha384', 'sha512'}


@onlygoogle
class TestGoogleRSA4096PKCS1v15SHA512(TestRSAPSSSHA256):
    address = "cloud+google:unimatrixdev/europe-west4/local/rsa_sign_pkcs1_4096_sha512"
    algorithm = 'sha512'
    padding = 'PKCS1v15'
    unsupported_signing_algorithms = {'sha256', 'sha384'}


@onlygoogle
class TestGoogleHMACSHA256(BaseSigning):
    address = "cloud+google:unimatrixdev/europe-west4/local/hmac_sha256"
    algorithm = 'sha256'
    has_identity = False
    unsupported_signing_algorithms = {'sha384', 'sha512'}
