"""Declares :class:`KeyRepository`."""
import copy
import typing

from google.cloud import kms
from .cryptokeyaddress import CryptoKeyAddress


ALGORITHM_PARAMS = {
    'HMAC_SHA256': {
        'capabilities': ['sig'],
        'secret': None,
        'sigalg': ['sha256']
    },
    'EC_SIGN_P256_SHA256': {
        'curve': "P-256",
        'capabilities': ['sig'],
        'sigalg': ['sha256']
    },
    'EC_SIGN_P384_SHA384': {
        'curve': "P-384",
        'capabilities': ['sig'],
        'sigalg': ['sha384']
    },
    'EC_SIGN_SECP256K1_SHA256': {
        'curve': "P-256K",
        'capabilities': ['sig'],
        'sigalg': ['sha256']
    },
    'RSA_SIGN_PSS_2048_SHA256': {
        'capabilities': ['sig'],
        'sigalg': ['sha256'],
        'size': 2048
    },
    'RSA_SIGN_PSS_3072_SHA256': {
        'capabilities': ['sig'],
        'sigalg': ['sha256'],
        'size': 3072
    },
    'RSA_SIGN_PSS_4096_SHA256': {
        'capabilities': ['sig'],
        'sigalg': ['sha256'],
        'size': 4096
    },
    'RSA_SIGN_PSS_4096_SHA512': {
        'capabilities': ['sig'],
        'sigalg': ['sha512'],
        'size': 4096
    },
    'RSA_SIGN_PKCS1_2048_SHA256': {
        'capabilities': ['sig'],
        'sigalg': ['sha256'],
        'size': 2048
    },
    'RSA_SIGN_PKCS1_3072_SHA256': {
        'capabilities': ['sig'],
        'sigalg': ['sha256'],
        'size': 3072
    },
    'RSA_SIGN_PKCS1_4096_SHA256': {
        'capabilities': ['sig'],
        'sigalg': ['sha256'],
        'size': 4096
    },
    'RSA_SIGN_PKCS1_4096_SHA512': {
        'capabilities': ['sig'],
        'sigalg': ['sha512'],
        'size': 4096
    },
}

PUBLIC_KEY_ALGORITHMS = {
    'EC_SIGN_P256_SHA256',
    'EC_SIGN_P384_SHA384',
    'EC_SIGN_SECP256K1_SHA256',
    'RSA_SIGN_PSS_2048_SHA256',
    'RSA_SIGN_PSS_3072_SHA256',
    'RSA_SIGN_PSS_4096_SHA256',
    'RSA_SIGN_PSS_4096_SHA512',
    'RSA_SIGN_PKCS1_2048_SHA256',
    'RSA_SIGN_PKCS1_3072_SHA256',
    'RSA_SIGN_PKCS1_4096_SHA256',
    'RSA_SIGN_PKCS1_4096_SHA512',
}


class KeyRepository:
    _cache: dict = {}
    _versions: dict = {}
    timeout: int = 15

    @property
    def client(self) -> kms.KeyManagementServiceAsyncClient:
        return kms.KeyManagementServiceAsyncClient()

    def __init__(self):
        self._cache = KeyRepository._cache

    async def get(self, address: CryptoKeyAddress) -> dict:
        public = None
        k = str(address)
        if k not in self._cache:
            async with self.client as client:
                version = await client.get_crypto_key_version(
                    request={'name': address.as_version(client)},
                    timeout=self.timeout
                )
                algorithm = version.algorithm.name
                params = copy.deepcopy(ALGORITHM_PARAMS[algorithm])
                if algorithm in PUBLIC_KEY_ALGORITHMS:
                    public = await client.get_public_key({'name': version.name})
            self._cache[k] = (
                algorithm,
                params,
                str.encode(public.pem) if public else None
            )
        assert k in self._cache # nosec
        return self._cache[k]

    async def get_versions(self, address: CryptoKeyAddress) -> typing.List[str]:
        """Return the list of version for the given path."""
        k = str(address)
        if k not in self._versions:
            versions = []
            async with self.client as client:
                response = client.list_crypto_key_versions(
                    request={
                        'parent': address.as_key(client),
                        'filter': "state=ENABLED"
                    },
                    timeout=self.timeout
                )
                async for version in await response:
                    versions.append(CryptoKeyAddress.frompath(version.name))
            self._versions[k] = versions
        assert k in self._versions # nosec
        return self._versions[k]
