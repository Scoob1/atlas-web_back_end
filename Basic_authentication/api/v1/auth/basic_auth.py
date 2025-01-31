#!/usr/bin/env python3
""" Basic Authentication module
"""
from api.v1.auth.auth import Auth
from typing import List

class BasicAuth(Auth):
    """Handles basic authentication"""
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Returns Base64 part of Authorization header if valid"""
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes Base64 string to UTF-8"""
        import base64
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except (TypeError, ValueError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
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
