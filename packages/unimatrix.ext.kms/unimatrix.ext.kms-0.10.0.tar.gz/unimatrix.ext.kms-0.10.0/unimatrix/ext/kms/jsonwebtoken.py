"""Declares :class:`JSONWebToken`."""
import json
import time
import typing

from .keychain import Keychain
from .utils import b64decode
from .exceptions import InvalidAudience
from .exceptions import InvalidClaim
from .exceptions import InvalidSignature
from .exceptions import MissingClaims
from .exceptions import TokenExpired
from .exceptions import TokenNotEffective
from .exceptions import UnknownIssuer
from .exceptions import UntrustedIssuer
from .joseheader import JOSEHeader
from .josesignature import Signature
from .jsonwebkeyset import JSONWebKeySet


class JSONWebToken:
    """Implements an interface to decode, verify the signatures of, modify,
    and validate JSON Web Tokens (JWTs).
    """
    __module__: str = 'unimatrix.ext.kms'

    @classmethod
    def decode(cls: type, obj: typing.Union[bytes, dict, str]):
        """Decode a JSON Web Token (JWT). Does not perform signature validation
        or decryption.

        Returns:
            :class:`unimatrix.ext.kms.JSONWebToken`
        """
        if isinstance(obj, dict): # pragma: no cover
            raise NotImplementedError
        if isinstance(obj, bytes):
            obj = bytes.decode(obj, 'ascii')
        header = JOSEHeader.parse(obj)
        if header.type == 'JWE': # pragma: no cover
            raise NotImplementedError
        assert header.type == 'JWS' # nosec
        protected, payload, signature =  str.split(obj, '.')
        instance = cls(
            header=header,
            claims=json.loads(b64decode(payload)),
            message=str.encode(f'{protected}.{payload}', 'ascii'),
            signatures=[Signature(header, protected, signature)]
        )
        return instance

    @classmethod
    def decrypt(cls) -> typing.Tuple[JOSEHeader, str]:
        raise NotImplementedError

    @classmethod
    def new(cls, **claims):
        """Return a new :class:`JSONWebToken`."""
        return cls(None, claims)

    def __init__(self,
        header: JOSEHeader,
        claims: dict,
        message: bytes = None,
        signatures: typing.List[Signature] = None
    ):
        self._header = header
        self._claims = claims
        self._payload = message
        self._signatures = signatures
        self._errors = []

    @property
    def iss(self) -> str:
        """Return the ``iss`` claim, or ``None``."""
        claim = self._claims.get('iss')
        if claim is not None and not isinstance(claim, str):
            raise InvalidClaim('iss')
        return claim

    @property
    def sub(self) -> typing.Any:
        """Return the ``sub`` claim, or ``None``."""
        return self._claims.get('sub')

    @property
    def aud(self) -> set:
        """Return the ``aud`` claim, or an empty set."""
        claim = self._claims.get('aud')
        if claim is None: # pragma: no cover
            return set()
        if not isinstance(claim, (list, str)):
            raise InvalidClaim('iss')
        if not isinstance(claim, list):
            claim = [claim]
        if not all([isinstance(x, str) for x in claim]):
            raise InvalidClaim('iss')
        return set(sorted(claim))

    @property
    def exp(self) -> int:
        """Return the ``exp`` claim, or ``None``."""
        return self._get_int('exp')

    @property
    def nbf(self) -> int:
        """Return the ``nbf`` claim, or ``None``."""
        return self._get_int('nbf')

    @property
    def iat(self) -> int:
        """Return the ``iat`` claim, or ``None``."""
        return self._get_int('iat')

    @property
    def jti(self) -> str:
        """Return the ``jti`` claim, or ``None``."""
        return self._claims.get('jti')

    def get(self, name: str):
        """Return the claim `name`, or ``None``."""
        return self._claims.get(name)

    def _get_int(self, name: str):
        claim = self._claims.get(name)
        if claim is not None and not isinstance(claim, int):
            raise InvalidClaim(name)
        return claim

    async def verify_signature(self,
        verifier: typing.Union[Keychain, JSONWebKeySet]
    ) -> bool:
        """Verifies a JSON Web Signature (JWS) using `keychain`."""
        if len(self._signatures) > 1:
            raise NotImplementedError
        if not await self._signatures[0].verify(verifier, self._payload):
            raise InvalidSignature
        return True

    def validate(self,
        issuer: str = None,
        audience: set = None,
        required: set = None,
        _now: int = None
    ) -> None:
        """Validate the claims presented by the JSON Web Token (JWT).

        This method raises an exceptio on errors.
        """
        now = int(_now) if _now else int(time.time())
        self._validate_exp(now)
        self._validate_nbf(now)
        self._validate_iss(issuer)
        self._validate_aud(audience)
        self._validate_required(required)

    def _validate_exp(self, now: int):
        exp = self._get_int('exp')
        if exp is not None and exp <= now:
            raise TokenExpired

    def _validate_nbf(self, now: int):
        nbf = self._get_int('nbf')
        if nbf is not None and nbf > now:
            raise TokenNotEffective

    def _validate_iss(self, issuer: str):
        if issuer is None:
            return
        if issuer != self.iss:
            if self.iss is None:
                raise UnknownIssuer
            else:
                raise UntrustedIssuer

    def _validate_aud(self, audience: set):
        # The "aud" (audience) claim identifies the recipients that the JWT is
        # intended for.  Each principal intended to process the JWT MUST
        # identify itself with a value in the audience claim.  If the principal
        # processing the claim does not identify itself with a value in the
        # "aud" claim when this claim is present, then the JWT MUST be
        # rejected.  In the general case, the "aud" value is an array of case-
        # sensitive strings, each containing a StringOrURI value.  In the
        # special case when the JWT has one audience, the "aud" value MAY be a
        # single case-sensitive string containing a StringOrURI value.  The
        # interpretation of audience values is generally application specific.
        # Use of this claim is OPTIONAL (RFC7519).
        if audience is None:
            return
        if not (self.aud & audience):
            raise InvalidAudience.with_detail(
                asserted=self.aud,
                required=list(sorted(audience))
            )

    def _validate_required(self, required: set):
        missing = set()
        for claim in (required or set()):
            if self._claims.get(claim) is not None:
                continue
            missing.add(claim)
        if missing:
            raise MissingClaims(list(sorted(missing)))
