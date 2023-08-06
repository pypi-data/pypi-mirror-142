"""Declares exceptions related to :mod:`unimatrix.ext.kms` failures."""
import logging

from unimatrix.exceptions import CanonicalException


class KeyImportError(LookupError): # pragma: no cover
    """Raised when the library tries to lookup a key that does not exist at
    the given address.
    """

    def __init__(self, urn: str):
        self.urn = urn

    def log(self, logger: logging.Logger) -> None:
        """Log the exception using the given `logger`."""
        logger.error("Unable to load key from source (%s)", self.urn)


class UnsupportedSigningAlgorithm(Exception):
    """Raised when a signing operation is attempted with an unsupported
    signing algorithm.
    """

    def __init__(self, algorithm: str, supported: set = None):
        self.algorithm = algorithm
        self.supported = supported


class JOSEException(CanonicalException):
    http_status_code = 403
    message = (
        "The provided JSON Web Token (JWT) could not be decoded, was malformed,"
        " expired, could not be decrypted or its signature did not validate."
    )

    def __init__(self, message: str = None):
        super().__init__(message=message)


class MalformedToken(JOSEException):
    code = "MALFORMED_TOKEN"


class UnsupportedAlgorithm(JOSEException):
    code = "UNSUPPORTED_ALGORITHM"

    def __init__(self, supported: set, **kwargs):
        message = (
            "The JOSE header specified an unsupported algorithm. Supported "
            f"algorithms are: {', '.join(sorted(supported))}."
        )
        super().__init__(message=message, **kwargs)


class UnsupportedEncryption(JOSEException):
    code = "UNSUPPORTED_CONTENT_ENCRYPTION"

    def __init__(self, supported: set, **kwargs):
        message = (
            "The server understood the JOSE header but the content of the JWE "
            "is encrypted using an unsupported algorithm. Supported algorithms "
            f"are {', '.join(sorted(supported))}."
        )
        super().__init__(message=message, **kwargs)


class TrustIssues(JOSEException):
    code = "TRUST_ISSUES"


class InvalidSignature(JOSEException):
    code = "INVALID_SIGNATURE"
    message = "The JSON Web Signature (JWS) could not be verified."


class InvalidClaim(JOSEException):
    code = "INVALID_CLAIM"

    def __init__(self, claim: str):
        super().__init__(
            f'The `{claim}` contains an illegal value.'
        )


class TokenExpired(JOSEException):
    code = "TOKEN_EXPIRED"
    message = "The JSON Web Token (JWT) is expired."


class TokenNotEffective(JOSEException):
    code = "TOKEN_NOT_EFFECTIVE"
    message = "The JSON Web Token (JWT) is not effective yet."


class UnknownIssuer(JOSEException):
    code = "UNKNOWN_ISSUER"
    message = "The issuer of the JSON Web Token (JWT) could not be determined."


class UntrustedIssuer(JOSEException):
    code = "UNTRUSTED_ISSUER"
    message = "The issuer of the JSON Web Token (JWT) is not trusted."


class InvalidAudience(JOSEException):
    code = "INVALID_AUDIENCE"
    message = "The audience of the JSON Web Token (JWT) is invalid."

    @classmethod
    def with_detail(cls, asserted: list, required: list):
        asserted = [x[:128] for x in asserted]
        return cls(
            message=(
                "Audience(s): {str.join(', ', asserted)} did not intersect with"
                " {str.join(', ', required)}."
            )
        )


class MissingClaims(JOSEException):
    code = "MISSING_CLAIMS"

    def __init__(self, missing: list):
        super().__init__(
            f'The JSON Web Token (JWT) must specify the following claims: '
            f'{", ".join(missing)}'
        )
