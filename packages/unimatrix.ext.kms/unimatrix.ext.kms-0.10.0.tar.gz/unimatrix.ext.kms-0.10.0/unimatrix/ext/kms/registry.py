"""Declares :class:`Registry`."""
import typing

from .model import VersionedKey


class Registry:
    """Maintains a registry of signing and/or encryption keys."""
    _keys: dict = {}
    reserved_names: str = {'self'}

    def delete(self, name: str) -> None:
        if name in self._keys:
            key = self._keys.pop(name)
            del key

    def get(self, name: str) -> VersionedKey:
        return self._keys[name]

    async def register(self,
        name: str,
        versions: list,
        usage: list
    ) -> VersionedKey:
        """Register key versions under `name`."""
        if name in self._keys:
            raise ValueError(f"Key already registered: {name}.")
        if len(versions) == 0:
            raise ValueError("Provide at least one key address.")
        if name in self.reserved_names:
            raise ValueError(f"Use a different name, '{name}' is reserved.")
        self._keys[name] = await VersionedKey.fromversions(versions, usage)
        return self._keys[name]


registry = Registry()
del Registry


def get(name: str) -> VersionedKey:
    """Lookup the preconfigured key that is identified by `name`."""
    return registry.get(name)


def unregister(name: str) -> None:
    """Unregister the named key from the registry."""
    return registry.delete(name)


async def register(
    name: str,
    versions: typing.List[
        typing.Union[dict, str]
    ] = None,
    usage: typing.List[
        typing.Literal['sig', 'enc']
    ] = None
) -> None:
    """Registers a private key under `name` using the given list of URLs
    `versions`. Supported URL schemes are:

    - ``cloud`` - A cloud key management service provider, either
      ``cloud.google.com`` or ``azure.microsoft.com``. If the cloud provider
      supports key versioning, then the latest key version is used as the
      default for all cryptographic operations, unless the `url` points to a
      specific key version.
    - ``literal`` - The literal key.
    - ``env`` - Load the key from an environment variable. This is only
      available for HMAC/SHA and elliptic curve algorithms.
    - ``file`` - A key that lives on the local filesystem.
    - ``settings+literal`` - Load the key from the ``settings`` module with
      the attribute being the key material. Like ``env``, is only available
      for HMAC/SHA and elliptic curve algorithms.
    - ``settings+file`` - Load the key from the ``settings`` module with
      the attribute being the absolute or relative path to the key material.

    Note that the first item in the list is considered the default key for
    all cryptographic operations.

    Examples:

    .. code:: python

        from unimatrix.ext import kms

        # Load a single key.
        kms.register('local', ['file+pem:pki/p256.key'])

        # Load multiple keys, allow signing operations only.
        kms.register('local-versioned', [
            'file+pem:pki/rsa.key',
            'file+pem:pki/p256.key',
            'file+pem:pki/p256k.key',
            ],
            usage=['sig']
        )

        # Import the latest key version (newlines added for brevity).
        kms.register('remote', [
            'cloud://cloud.google.com/projects'
            '/unimatrixdev/locations/europe-west4'
            '/keyRings/local/cryptoKeys/ec_sign_p256_sha256'
        ])

        # Import a specific key version (newlines added for brevity).
        kms.register('remote-versioned', [
            'cloud://cloud.google.com/projects'
            '/unimatrixdev/locations/europe-west4'
            '/keyRings/local/cryptoKeys/ec_sign_p256_sha256/cryptoKeyVersions/5'
        ])
    """
    if isinstance(versions, (dict, str)):
        versions = [versions]
    key = await registry.register(name, versions, usage)
    await key.load()
    return key
