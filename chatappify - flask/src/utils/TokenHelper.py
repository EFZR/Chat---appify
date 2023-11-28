import jwt, string, random
from werkzeug.exceptions import BadRequest
from flask import session, current_app


class TokenHelper:
    @staticmethod
    def decode_token(token):
        """Decode a JWT token and return the payload

        Args:
            token (str): The JWT token to decode

        Raises:
            BadRequest: If the token is invalid or expired

        Returns:
            dict: the decoded payload JWT token
        """
        try:
            payload = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            return payload
        except jwt.ExpiredSignatureError:
            session.clear()
            raise BadRequest("Time to token expired")
        except (jwt.InvalidTokenError, jwt.DecodeError):
            session.clear()
            raise BadRequest("Invalid token")

    @staticmethod
    def verify_token(request):
        """Verify a JWT token from a request header

        Args:
            request: The flask request object

        Raises:
            BadRequest: If the token is not found or verification fails

        Returns:
            dict: the decoded payload JWT token
        """
        header = request.headers.get("Authorization")
        if not header:
            raise BadRequest("Token not found")
        token = header.split(" ")[1]
        return TokenHelper.decode_token(token)
    
    @staticmethod
    def generate_secret_key(length=20):
        """Generate a random secret key

        Args:
            length (int, optional): Size of the secret key. Defaults to 20.

        Returns:
            str: the secret key
        """
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))