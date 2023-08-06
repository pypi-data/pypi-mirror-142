# pylint: skip-file
import time
import pytest

from ..exceptions import InvalidAudience
from ..exceptions import MissingClaims
from ..exceptions import TokenExpired
from ..exceptions import TokenNotEffective
from ..exceptions import UnknownIssuer
from ..exceptions import UntrustedIssuer
from ..jsonwebtoken import JSONWebToken


class TestJSONWebToken:

    def test_validate_expires_unset(self):
        token = JSONWebToken.new(
            exp=None
        )
        token.validate()

    def test_validate_expires_future(self):
        token = JSONWebToken.new(
            exp=int(time.time() + 5)
        )
        token.validate()

    def test_validate_expires_past(self):
        token = JSONWebToken.new(
            exp=int(time.time() - 5)
        )
        with pytest.raises(TokenExpired):
            token.validate()

    def test_validate_nbf_unset(self):
        token = JSONWebToken.new()
        token.validate()

    def test_validate_nbf_future(self):
        token = JSONWebToken.new(
            nbf=int(time.time() + 5)
        )
        with pytest.raises(TokenNotEffective):
            token.validate()

    def test_validate_nbf_past(self):
        token = JSONWebToken.new(
            nbf=int(time.time() - 5)
        )
        token.validate()

    def test_validate_issuer_valid(self):
        token = JSONWebToken.new(iss='foo')
        token.validate(issuer="foo")

    def test_validate_issuer_valid_none(self):
        token = JSONWebToken.new(iss='foo')
        token.validate(issuer=None)

    def test_validate_issuer_unknown(self):
        token = JSONWebToken.new()
        with pytest.raises(UnknownIssuer):
            token.validate(issuer="foo")

    def test_validate_issuer_untrusted(self):
        token = JSONWebToken.new(iss="bar")
        with pytest.raises(UntrustedIssuer):
            token.validate(issuer="foo")

    def test_validate_audience_valid(self):
        token = JSONWebToken.new(aud="foo")
        token.validate(audience={"foo"})

        token = JSONWebToken.new(aud=["foo"])
        token.validate(audience={"foo"})

        token = JSONWebToken.new(aud=["foo"])
        token.validate(audience=None)

        token = JSONWebToken.new(aud="foo")
        token.validate(audience={"foo", "bar"})

        token = JSONWebToken.new(aud=["foo"])
        token.validate(audience={"foo", "bar"})

    def test_validate_audience_invalid(self):
        token = JSONWebToken.new(aud="foo")
        with pytest.raises(InvalidAudience):
            token.validate(audience={"bar"})

        token = JSONWebToken.new(aud=["foo", "bar"])
        with pytest.raises(InvalidAudience):
            token.validate(audience={"baz"})

        token = JSONWebToken.new(aud=None)
        with pytest.raises(InvalidAudience):
            token.validate(audience={"baz"})

        token = JSONWebToken.new()
        with pytest.raises(InvalidAudience):
            token.validate(audience={"baz"})

    def test_validate_required_claims(self):
        token = JSONWebToken.new(foo="foo")
        token.validate(required={"foo"})

    def test_validate_required_claims_missing(self):
        token = JSONWebToken.new(foo="foo")
        with pytest.raises(MissingClaims):
            token.validate(required={"bar"})

    def test_validate_required_claims_none(self):
        token = JSONWebToken.new(bar=None)
        with pytest.raises(MissingClaims):
            token.validate(required={"bar"})
