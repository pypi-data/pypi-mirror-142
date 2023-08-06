from unimatrix.ext import kms
import asyncio


async def main():
    print(await kms.discover_jwks("https://accounts.google.com"))


asyncio.run(main())
