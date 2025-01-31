#!/usr/bin/env python3
""" Basic Authentication module
"""

import base64
from typing import List


class BasicAuth:
    """Basic authentication class inheriting from Auth"""
    
    def __init__(self):
        # Import the Auth class dynamically inside the method to avoid circular imports
        from api.v1.auth.auth import Auth
        self.auth = Auth()

    # Implement or override necessary methods
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return self.auth.require_auth(path, excluded_paths)

    def authorization_header(self, request=None) -> str:
        return self.auth.authorization_header(request)

    def current_user(self, request=None):
        return self.auth.current_user(request)

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes the Base64 part of the Authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts the email and password from the Base64 decoded string"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password
