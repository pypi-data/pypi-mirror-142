"""Declares :class:`CryptoKeyAddress`."""
from google.cloud import kms


class CryptoKeyAddress:

    @classmethod
    def frompath(cls, path: str):
        parts = str.split(path, '/')
        return cls(parts[1], parts[3], parts[5], parts[7], parts[9])

    @classmethod
    def parse(cls, address: str):
        return cls(*str.split(address, '/'))

    def __init__(self,
        project: str,
        location: str,
        keyring: str,
        key: str,
        version: str = None
    ):
        """The address of a key that is managed with Google Cloud KMS. May
        optionally specify a version indicator.
        """
        self._project = project
        self._location = location
        self._keyring = keyring
        self._key = key
        self._version = version

    def as_key(self, client: kms.KeyManagementServiceAsyncClient) -> str:
        return client.crypto_key_path(
            project=self._project,
            location=self._location,
            key_ring=self._keyring,
            crypto_key=self._key,
        )

    def as_version(self, client: kms.KeyManagementServiceAsyncClient) -> str:
        return client.crypto_key_version_path(
            project=self._project,
            location=self._location,
            key_ring=self._keyring,
            crypto_key=self._key,
            crypto_key_version=self._version
        )

    def __str__(self) -> str:
        value = f'{self._project}/{self._location}/{self._keyring}/{self._key}'
        if self._version:
            value = f'{value}/{self._version}'
        return value

    def __hash__(self) -> str:
        return str(self).__hash__()
