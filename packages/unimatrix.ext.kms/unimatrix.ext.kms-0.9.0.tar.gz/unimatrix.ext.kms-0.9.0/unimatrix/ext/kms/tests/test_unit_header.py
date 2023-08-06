# pylint: skip-file
import base64

import jwt
import pytest

from ..exceptions import MalformedToken
from ..exceptions import UnsupportedAlgorithm
from ..exceptions import UnsupportedEncryption
from ..joseheader import JOSEHeader



class TestJOSEHeader:

    @pytest.fixture
    def jws(self):
        return jwt.encode({"foo": "bar"}, "secret", algorithm="HS256")

    def test_invalid_json_raises(self):
        with pytest.raises(MalformedToken):
            JOSEHeader.parse(base64.b64encode(b'foo') + b'.bar.baz')

    def test_invalid_type_raises(self):
        with pytest.raises(TypeError):
            JOSEHeader.parse(None)

    def test_unknown_type_raises(self):
        with pytest.raises(MalformedToken):
            JOSEHeader(
                algorithm='HS256',
                kind='foo',
                segments=3
            )

    def test_unknown_algorithm_raises(self):
        with pytest.raises(UnsupportedAlgorithm):
            JOSEHeader(
                algorithm='foo',
                segments=3
            )

    def test_invalid_algorithm_raises(self):
        with pytest.raises(UnsupportedAlgorithm):
            JOSEHeader(
                algorithm='RSA1_5',
                segments=3
            )

    def test_unknown_algorithm_with_known_encryption_raises(self):
        with pytest.raises(UnsupportedAlgorithm):
            JOSEHeader(
                algorithm='foo',
                encryption="A128CBC-HS256",
                segments=5
            )

    def test_invalid_algorithm_with_known_encryption_raises(self):
        with pytest.raises(UnsupportedAlgorithm):
            JOSEHeader(
                algorithm='HS256',
                encryption="A128CBC-HS256",
                segments=5
            )

    def test_signing(self):
        with pytest.raises(MalformedToken):
            JOSEHeader(
                algorithm='HS256',
                segments=5
            )

    def test_encryption_requires_segments(self):
        with pytest.raises(MalformedToken):
            JOSEHeader(
                algorithm='RSA1_5',
                encryption="A128CBC-HS256",
                segments=3
            )

    def test_known_algorithm_with_unknown_encryption_raises(self):
        with pytest.raises(UnsupportedEncryption):
            JOSEHeader(
                algorithm='RSA1_5',
                encryption="foo",
                segments=5
            )

    def test_invalid_segments_raises(self, jws):
        with pytest.raises(MalformedToken):
            JOSEHeader.parse(jws + '.foo')

    def test_parse_header_jws(self, jws):
        header = JOSEHeader.parse(jws)
        assert header.type == 'JWS'

    def test_no_segments_raises(self, jws):
        with pytest.raises(MalformedToken):
            JOSEHeader.parse(jws.replace('.', ''))

    def test_undecodable_raises(self, jws):
        with pytest.raises(MalformedToken):
            JOSEHeader.parse('a.b.c')
