#!/usr/bin/env python3
""" Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Template for authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user"""
        return None
