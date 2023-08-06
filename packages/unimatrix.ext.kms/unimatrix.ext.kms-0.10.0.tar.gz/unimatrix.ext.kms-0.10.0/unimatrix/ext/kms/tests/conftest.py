# pylint: skip-file
import asyncio
import json

import pytest

from ..const import TEST_HMAC_KEY
from ..jsonwebkeyset import JSONWebKeySet
from ..jsonwebtoken import JSONWebToken
from ..keychain import Keychain
from ..utils import b64decode


JWKS = """{
  "keys": [
    {
      "e": "AQAB",
      "kty": "RSA",
      "kid": "3dd6ca2a81dc2fea8c3642431e7e296d2d75b446",
      "alg": "RS256",
      "use": "sig",
      "n": "urIBEeEj2HvBoNipv4PcFPGbw66boVQx60hl0sK7rTLKpLZqIkorKiC2d8nDg7Zrm_uYvYBNsoQWZohEsTh3kBSs92BNnbA_Z1Ok345e8BGDKifsi6YuMtjqffIqsZs-gCWE_AxZ_9m-CfCzs5UGgad7E0qFQxlOe18ds-mHhWd3l-CgQsAYNMoII7GCxLsp5GUaPFjld5E9h5dK7LrKH311swII_rypnK6ktduKpcuMLuxcfz8oQ3Gqzp1oZ1fm9eG98adjSLl796vz5Uh-mz__YBkyD67Jibf4pqtQ07skq_Ff7KKQO32I4Yy0Dp7I0aUTYA2ff8JT0Huz2876LQ"
    },
    {
      "alg": "RS256",
      "n": "rXzt9xpKC1vqbtVm-XJi2ys1_4LaiRKBhBNyUTtTBZedgJtr3XU6SSol8HEDwzAuPb3cODABr0wpNmEGFg7dcSL6QOSSb3sntvsiYqxUXIFnFpAGMEA2SzconFLdAaLNKAX1T4F1EU50v20EIZFxWdR8sZ0ClrOrixPf_TR2hRoqiyvrpEyeVxxWatae2DPTmgeTmdanPAKjspR9iF4xEpRoo2MKUGGMDDZvFJSSlL1Bd26SbXEHYvn4muOLWuaro4Va2HUPnfDXJEPPAr2Mag1sbiEMgjs0FUlfJkk_oZr8GEOny4TOlhGmJmrPCkunGj3yAmwOmDULpjRihknkpw",
      "e": "AQAB",
      "kty": "RSA",
      "kid": "d63dbe73aad88c854de0d8d6c014c36dc25c4292",
      "use": "sig"
    }
  ]
}"""


PROTECTED, PAYLOAD, SIG = str.split('eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ2M2RiZTczYWFkODhjODU0ZGUwZDhkNmMwMTRjMzZkYzI1YzQyOTIiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJodHRwczovL21vbGFuby11cGxpbmstbzd4MnBoenpzcS1lei5hLnJ1bi5hcHAvIiwiYXpwIjoiMTAyNTE0ODUxMzk5MzE4NzE2MTE3IiwiZW1haWwiOiJtb2xhbm8tdXBsaW5rQHVuaW1hdHJpeGluZnJhLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV4cCI6MTY0NjgwNjMwNiwiaWF0IjoxNjQ2ODAyNzA2LCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJzdWIiOiIxMDI1MTQ4NTEzOTkzMTg3MTYxMTcifQ.mJAFpF7uyye0703nNyu7xRuGDMkMtxMBR-mYCB0MvPVHF5dTQly3SameJDRuFjuZP6WVR3XVi50Ojmx7lSXLPsYMm0L1pVGOchUTSpYwifCTmkhx7DYVx2FdEIFvOD1iWe4EwVPaFXUpgHPycXLxsID2tU2D5QlgQjpw24rPr39t9oLeFGq4AUVcdCw-g7iYdQpm2TH9Ls4GW56Bit8lxKRHbh9kCYvJc1ntAIHsQ3QYyUV8Ew7CDiy5bGVuX-0uAP6KzNVr08gFalrvkRMD7gg2tkln1CdsbA4mGhq3wPBUGu1FAavVRchB3Z2IzksBnBaHLeml5RWAJX9BTgu9lw', '.')


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture
def jwks_json():
	return JWKS


@pytest.fixture
def jwks_dict(jwks_json):
	return json.loads(jwks_json)


@pytest.fixture
def jwks(jwks_dict):
    return JSONWebKeySet.fromdict(jwks_dict)


@pytest.fixture
def signature():
    return b64decode(SIG)


@pytest.fixture
def jws():
    return JSONWebToken.decode(f'{PROTECTED}.{PAYLOAD}.{SIG}')


@pytest.fixture
def message():
    return str.encode(f'{PROTECTED}.{PAYLOAD}')


@pytest.fixture(scope='session')
async def keychain():
    keychain = Keychain()
    await keychain.register('hmac', [f"literal+hmac:{TEST_HMAC_KEY}?keyid=hmac"])
    await keychain.register('rsa', ['file+pem:pki/rsa.key'])
    await keychain.register('p256', ['file+pem:pki/p256.key'])
    await keychain.register('p384', ['file+pem:pki/p384.key'])
    await keychain.register('p521', ['file+pem:pki/p521.key'])

    return keychain
