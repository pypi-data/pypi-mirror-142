"""Declares :class:`Keychain`."""
import typing

import aiohttp

from .jsonwebkey import JSONWebKey
from .jsonwebkeyset import JSONWebKeySet
from .model import KeyVersion
from .model import VersionedKey
from .presets import get as preset_factory


class Keychain:
    """Provides an interface to manage public and private keys."""

    @staticmethod
    async def get_issuer_metadata(
        session: aiohttp.ClientSession,
        url: str
    ) -> dict:
        """Discover the metadata for the given `url`, which is an OpenID
        or OAuth 2.0 authorization server.
        """
        response = await session.get(
            f'{url}/.well-known/oauth-authorization-server'
        )
        if response.status == 404:
            response = await session.get(
                f'{url}/.well-known/openid-configuration'
            )
        if response.status == 404:
            return None
        return await response.json()

    def __init__(self):
        self._jwks = {}
        self._public = {}
        self._keys = {}
        self._versions = {}

    def get(self, name: str, private: bool = False):
        """Lookup a key from the :class:`Keychain`."""
        if name in self._versions:
            manager = self._versions.get(name)
            key = manager._default
        else:
            key = self._keys.get(name)
        return key

    async def register(self,
        name: str,
        versions: typing.Union[list, str]
    ) -> None:
        """Registers a signing or encryption key from the given source."""
        if isinstance(versions, (dict, str)):
            versions = [versions]

        key = await VersionedKey.fromversions(versions, ['sig'])
        await key.load()
        await self.persist(key, name=name)
        return key

    async def discover_jwks(self, issuer: str) -> None:
        """Discover the JSON Web Key Set (JWKS) for the specified `issuer`.

        Query the OpenID/OAuth 2.0 discovery endpoints to determine the
        ``jwks_uri`` value. Import the retrieved JWKS and persist it for the
        given `issuer`.
        """
        if issuer in self._jwks:
            return self._jwks[issuer]

        jwks = None
        async with aiohttp.ClientSession() as session:
            metadata = await self.get_issuer_metadata(session, issuer)
            if metadata and 'jwks_uri' in metadata:
                jwks_uri = metadata.get('jwks_uri')
                if jwks_uri:
                    response = await session.get(jwks_uri)
                    jwks = JSONWebKeySet.fromdict(await response.json())
                    await self.persist(jwks, issuer=issuer)

        return jwks

    async def get_issuer_jwks(self,
        issuer: str
    ) -> typing.Union[JSONWebKeySet, None]:
        """Return the :class:`~unimatrix.ext.kms.JSONWebKeySet` for the given
        `issuer`, or ``None`` if no JWKS was registered.
        """
        return self._jwks.get(issuer)

    async def persist(self, obj, **kwargs):
        """Persist an object in the keychain. Supported types are:

        - :class:`~unimatrix.ext.kms.JSONWebKeySet`
        - :class:`~unimatrix.ext.kms.JSONWebKey`
        """
        if isinstance(obj, JSONWebKeySet):
            return await self.persist_jwks(obj, **kwargs)
        elif isinstance(obj, JSONWebKey):
            return await self.persist_jwk(obj)
        elif isinstance(obj, KeyVersion):
            return await self.persist_key_version(obj)
        elif isinstance(obj, VersionedKey):
            return await self.persist_versioned_key(obj, **kwargs)
        else:
            raise NotImplementedError(type(obj))

    async def persist_jwks(self, jwks: JSONWebKeySet, issuer: str):
        """Persist a :class:`JSONWebKeySet` for a specific `issuer`."""
        self._jwks[issuer] = jwks
        for key in jwks:
            await self.persist(key)

    async def persist_jwk(self, jwk: JSONWebKey):
        """Persist a :class:`JSONWebKey` by its key identifier."""
        if jwk.kid is None:
            raise ValueError("Can not persist keys without a key identifier.")
        self._public[jwk.kid] = jwk

    async def persist_key_version(self, key: KeyVersion):
        """Persist a :class:`KeyVersion` by its key identifying. As these
        objects are never fetched from remote sources or cached, but solely
        configured at application boot time, these must not be stored anywhere
        else than in local memory.
        """
        self._keys[key.keyid] = key

    async def persist_versioned_key(self, key: VersionedKey, name: str):
        """Persist a :class:`VersionedKey` by its name."""
        self._versions[name] = key
        for version in key:
            await self.persist(version)

    async def unregister(self, name: str):
        """Unregister the signing/encryption key `name`."""
        self._keys.pop(name, None)

    async def verify(self,
        signature: bytes,
        payload: bytes,
        algorithm: str,
        using: str,
        prehashed: bool = False
    ) -> bool:
        """Verify a signature with the given key and algorithm. Return a
        boolean indicating if `signature` was valid for `payload`.

        The `algorithm` must be a string identifying one of the JSON Web
        Algorithms (JWA) supported by :mod:`unimatrix.ext.kms`.

        The `using` argument must point to a preregistered key for this
        :class:`Keychain` instance.

        The `prehashed` argument indicates if `payload` is a proper digest for
        the chosen signature algorithm. If `prehashed` is ``False``, then
        `payload` is hashed prior to verification against the signature.
        """
        key = self.get(using)
        alg = preset_factory(algorithm)

        # Bail out early if there is no key to verify the signature.
        if key is None:
            return False

        return await alg.verify(key, signature, payload, prehashed=prehashed)


keychain: Keychain = Keychain()


def discover_jwks(issuer: str):
    """Discover the JSON Web Key Set (JWKS) for the given `issuer` using the
    default keychain, and persist it for subsequent use.
    """
    return keychain.discover_jwks(issuer)


def get_issuer_jwks(issuer: str) -> typing.Union[JSONWebKeySet, None]:
    """Return the :class:`~unimatrix.ext.kms.JSONWebKeySet` for the given
    `issuer`, or ``None`` if no JWKS was registered.
    """
    return keychain.get_issuer_jwks(issuer)
