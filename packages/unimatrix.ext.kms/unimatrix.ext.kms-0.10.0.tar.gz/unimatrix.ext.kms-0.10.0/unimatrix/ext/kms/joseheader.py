"""Declares :class:`JOSEHeader`."""
import binascii
import json
import typing

from .exceptions import MalformedToken
from .exceptions import UnsupportedAlgorithm
from .exceptions import UnsupportedEncryption
from .utils import b64decode


class JOSEHeader:
    """Represents the header of a JSON Web Token (JWT)."""
    __module__ = 'unimatrix.ext.kms.jose'
    _encalgs: set = {
        "RSA1_5",
        "RSA-OAEP",
        "RSA-OAEP-256",
        "A128KW",
        "A192KW",
        "A256KW",
        "dir",
        "ECDH-ES",
        "ECDH-ES+A128KW",
        "ECDH-ES+A192KW",
        "ECDH-ES+A256KW",
        "A128GCMKW",
        "A192GCMKW",
        "A256GCMKW",
        "PBES2-HS256+A128KW",
        "PBES2-HS384+A192KW",
        "PBES2-HS512+A256KW",
    }

    _sigalgs: set = {
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
        "ES256",
        "ES384",
        "ES512",
        "PS256",
        "PS384",
        "PS512",
        "none"
    }

    _msgalgs = {
        "A128CBC-HS256",
        "A192CBC-HS384",
        "A256CBC-HS512",
        "A128GCM",
        "A192GCM",
        "A256GCM",
    }

    @property
    def algorithm(self) -> str:
        """Return the algorithm used to sign or encrypt the JWT."""
        return self._algorithm

    @property
    def kid(self) -> str:
        """Identifies the key that was used to sign/encrypt the
        JWT.
        """
        return self._keyid

    @property
    def type(self) -> typing.Literal['JWE', 'JWS', None]:
        """Return the type of JWT."""
        return self._type

    @classmethod
    def parse(cls, token: typing.Union[bytes, str]):
        """Parse a JSON Web Token into a :class:`JWT` object."""
        # 7.2.  Validating a JWT
        #
        # When validating a JWT, the following steps are performed.  The order
        # of the steps is not significant in cases where there are no
        # dependencies between the inputs and outputs of the steps.  If any of
        # the listed steps fail, then the JWT MUST be rejected -- that is,
        # treated by the application as an invalid input.
        #
        # 1.   Verify that the JWT contains at least one period ('.')
        #    character.
        #
        # 2.   Let the Encoded JOSE Header be the portion of the JWT before the
        #    first period ('.') character.
        #
        # 3.   Base64url decode the Encoded JOSE Header following the
        #    restriction that no line breaks, whitespace, or other additional
        #    characters have been used.
        #
        # 4.   Verify that the resulting octet sequence is a UTF-8-encoded
        #    representation of a completely valid JSON object conforming to
        #    RFC 7159 [RFC7159]; let the JOSE Header be this JSON object.
        #
        # 5.   Verify that the resulting JOSE Header includes only parameters
        #    and values whose syntax and semantics are both understood and
        #    supported or that are specified as being ignored when not
        #    understood.
        #
        # 6.   Determine whether the JWT is a JWS or a JWE using any of the
        #    methods described in Section 9 of [JWE].
        #
        # ....
        #
        # Finally, note that it is an application decision which algorithms may
        # be used in a given context.  Even if a JWT can be successfully
        # validated, unless the algorithms used in the JWT are acceptable to
        # the application, it SHOULD reject the JWT.
        if not isinstance(token, (bytes, str)):
            raise TypeError(f"Invalid type: {type(token)}")
        if isinstance(token, bytes):
            token = bytes.decode(token, 'ascii')
        i = token.find(b'.' if isinstance(token, bytes) else '.')
        if i == -1:
            raise MalformedToken(
                "Compact serialization of JWS/JWE requires 3 or 5 segments."
            )
        s = token[0:i]
        try:
            header = json.loads(b64decode(s))
        except binascii.Error:
            raise MalformedToken(
                "Could not decode URL-encoded header."
            )
        except json.decoder.JSONDecodeError:
            raise MalformedToken(
                "The JOSE header could not be deserialized as JSON."
            )
        return cls(
            algorithm=header.get('alg'),
            encryption=header.get('enc'),
            content_type=header.get('cty'),
            kind=header.get('typ'),
            keyid=header.get('kid'),
            critical=header.get('crit'),
            segments=token.count('.') + 1
        )

    def __init__(self,
        algorithm: str,
        encryption: str = None,
        content_type: str = None,
        kind: str = None,
        keyid: str = None,
        critical: list = None,
        segments: int = None
    ):
        """The JOSE Header describes the properties of a JSON Web Signature
        (JWS) or JSON Web Encryption (JWE).

        Args:
            algorithm (str): the algorithm used with the JWT, must be an
                algorithm specified in :rfc:`7518`, or a collision-resistant
                name that is understood by the application.
            encryption (str): the content encryption algorithm used for the
                JWE.
            content_type (str): describes the content type (e.g the ``cty``)
                header parameter.
            kind (str): the type of object contained (``typ`` header).
            keyid (str): the key identifier of the key that was used to
                encrypt or sign the JWT.
            critical (list): the list of header parameters that are considered
                critical.
            segments (int): the number of dot-separated segments of the input
                token.
        """
        self._algorithm = algorithm
        self._encryption = encryption
        self._content_type = content_type
        self._kind = kind
        self._keyid = keyid
        self._critical = set(critical or [])
        self._segments = segments
        self._type = None

        # Determine the type according to RFC 7516. If any of these fails,
        # the token is considered malformed (but the exception is not raised
        # here):
        #
        # 9.  Distinguishing between JWS and JWE Objects
        #
        # There are several ways of distinguishing whether an object is a JWS
        # or JWE.  All these methods will yield the same result for all legal
        # input values; they may yield different results for malformed inputs.
        #
        # o  If the object is using the JWS Compact Serialization or the JWE
        #    Compact Serialization, the number of base64url-encoded segments
        #    separated by period ('.') characters differs for JWSs and JWEs.
        #    JWSs have three segments separated by two period ('.') characters.
        #    JWEs have five segments separated by four period ('.') characters.
        #
        #    ....
        #
        # o  The JOSE Header for a JWS can be distinguished from the JOSE
        #    Header for a JWE by examining the "alg" (algorithm) Header
        #    Parameter value.  If the value represents a digital signature or
        #    MAC algorithm, or is the value "none", it is for a JWS; if it
        #    represents a Key Encryption, Key Wrapping, Direct Key Agreement,
        #    Key Agreement with Key Wrapping, or Direct Encryption algorithm,
        #    it is for a JWE.  (Extracting the "alg" value to examine is
        #    straightforward when using the JWS Compact Serialization or the
        #    JWE Compact Serialization and may be more difficult when using the
        #    JWS JSON Serialization or the JWE JSON Serialization.)
        #
        # o  The JOSE Header for a JWS can also be distinguished from the JOSE
        #    Header for a JWE by determining whether an "enc" (encryption
        #    algorithm) member exists.  If the "enc" member exists, it is a
        #    JWE; otherwise, it is a JWS.
        if self._segments is not None and self._segments not in (3,5):
            raise MalformedToken(
                message=(
                    "Invalid number of segments in JWS Compact Serialization "
                    f"or JWE Compact Serialization: {self._segments}"
                )
            )

        # Verify that we understand the type, if specified.
        if kind and str.lower(kind) != 'jwt':
            raise MalformedToken(
                "The server does not understand the value of the `typ` "
                "claim in the JOSE header."
            )

        # Verify that any algorithm we support was used.
        if self._algorithm not in (self._encalgs|self._sigalgs):
            raise UnsupportedAlgorithm(self._encalgs|self._sigalgs)

        # Verify that a supported signing/encryption algorithm was used.
        if self._encryption is not None:
            if self._segments is not None and self._segments != 5:
                raise MalformedToken(
                    "JWE Compact Serialization requires 5 segments."
                )
            if self._algorithm not in self._encalgs:
                raise UnsupportedAlgorithm(self._encalgs)
            if self._encryption not in self._msgalgs:
                raise UnsupportedEncryption(self._msgalgs)
            self._type = 'JWE' # pragma: no cover
        else:
            # This is most probably a JWS.
            if self._segments is not None and self._segments != 3:
                raise MalformedToken(
                    "JWS Compact Serialization requires 5 segments."
                )
            if self._algorithm not in self._sigalgs:
                raise UnsupportedAlgorithm(self._sigalgs)
            self._type = 'JWS'
