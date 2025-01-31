#!/usr/bin/env python3
""" Basic Authentication module
"""

class BasicAuth:
    """Basic authentication class inheriting from Auth"""

    def __init__(self):
        from api.v1.auth.auth import Auth
        self.auth = Auth()


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return self.auth.require_auth(path, excluded_paths)

    def authorization_header(self, request=None) -> str:
        return self.auth.authorization_header(request)

    def current_user(self, request=None):
        return self.auth.current_user(request)
