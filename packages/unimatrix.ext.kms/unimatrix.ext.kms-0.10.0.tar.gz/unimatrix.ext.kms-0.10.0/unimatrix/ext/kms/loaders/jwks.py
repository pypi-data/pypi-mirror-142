"""Declares :class:`JWKSLoader`."""
import logging

import aiohttp

from ..jsonwebkeyset import JSONWebKeySet

class JWKSLoader:
    logger: logging.Logger = logging.getLogger('uvicorn')

    async def discover(self, url: str, timeout: int = 5) -> JSONWebKeySet:
        """Inspect the OpeID/OAuth 2.0 metadata endpoints to find the
        server ``jwks_uri`` and return a :class:`JSONWebKeySet` instance
        containing the keys.
        """
        jwks = None
        timeout = aiohttp.ClientTimeout(total=timeout)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            metadata = (
                await self._get(
                    session=session,
                    url=f'{url}/.well-known/oauth-authorization-server'
                )
                or await self._get(
                    session=session,
                    url=f'{url}/.well-known/openid-configuration'
                )
            )
            if metadata and metadata.get('jwks_uri'):
                jwks = await self._get(session, metadata['jwks_uri'])
        return JSONWebKeySet.fromdict(jwks) if jwks else None

    async def _get(self, session, url):
        try:
            response = await session.get(url)
            return await response.json() if response.status < 300 else None
        except (aiohttp.ClientError, aiohttp.ClientResponseError) as e:
            self.logger.error("Caught fatal %s when retrieving %s", e, url)
            return None
