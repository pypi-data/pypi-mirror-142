# pylint: skip-file
import pytest

from ..exceptions import InvalidClaim
from ..jsonwebtoken import JSONWebToken


class TestTokenProperties:

    @pytest.fixture
    def token(self):
        return JSONWebToken(None, {
            'iss': "foo",
            'aud': "bar",
            'sub': "baz",
            'exp': 2,
            'iat': 0,
            'nbf': 1,
            'jti': 'taz'
        })

    def test_iss(self, token):
        assert token.iss == 'foo'

    def test_invalid_iss(self):
        with pytest.raises(InvalidClaim):
            token = JSONWebToken(None, {'iss': 0})
            assert token.iss != 0

    def test_aud(self, token):
        assert token.aud == {'bar'}

    def test_invalid_aud(self):
        with pytest.raises(InvalidClaim):
            token = JSONWebToken(None, {'aud': 0})
            assert token.aud != 0
        with pytest.raises(InvalidClaim):
            token = JSONWebToken(None, {'aud': [0]})
            assert token.aud != [0]

    def test_sub(self, token):
        assert token.sub == 'baz'

    def test_exp(self, token):
        assert token.exp == 2

    def test_invalid_exp(self):
        with pytest.raises(InvalidClaim):
            token = JSONWebToken(None, {'exp': 'a'})
            assert token.exp != 'a'

    def test_iat(self, token):
        assert token.iat == 0

    def test_invalid_iat(self):
        with pytest.raises(InvalidClaim):
            token = JSONWebToken(None, {'iat': 'a'})
            assert token.iat != 'a'

    def test_nbf(self, token):
        assert token.nbf == 1

    def test_invalid_nbf(self):
        with pytest.raises(InvalidClaim):
            token = JSONWebToken(None, {'nbf': 'a'})
            assert token.nbf != 'a'

    def test_jti(self, token):
        assert token.jti == 'taz'
