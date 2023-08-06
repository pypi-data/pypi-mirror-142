"""megaphone Authentication."""


from singer_sdk.authenticators import SimpleAuthenticator


class megaphoneAuthenticator(SimpleAuthenticator):
    """Authenticator class for megaphone."""

    @classmethod
    def create_for_stream(cls, stream) -> "megaphoneAuthenticator":
        return cls(
            stream=stream,
            auth_headers={
                "Authorization": "Token token=" + stream.config.get("auth_token")
            },
        )
