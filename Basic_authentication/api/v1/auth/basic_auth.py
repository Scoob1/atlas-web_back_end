#!/usr/bin/env python3
""" Basic Authentication module
"""
from api.v1.auth.auth import Auth
from typing import List
from typing import TypeVar, Tuple
from models.user import User


class BasicAuth(Auth):
    """Handles basic authentication"""

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """Extracts user email and password from the Base64 decoded value"""
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_pwd = decoded_base64_authorization_header.split(":", 1)
        return user_email, user_pwd

    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """Returns Base64 part of Authorization header if valid"""
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes Base64 string to UTF-8"""
        import base64
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except (TypeError, ValueError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Extracts email and password from decoded Base64 string"""
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(":", 1)

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if auth is required for path"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd:
                                     str) -> TypeVar('User'):
        """Returns User instance based on email and password"""
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        user = User.search({'email': user_email})
        if not user:
            return None

        user = user[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current User instance based on the request"""
        if request is None:
            return None

        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(authorization_header)
        if base64_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
