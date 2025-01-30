#!/usr/bin/env python3
""" Basic Authentication module
"""

# avoiding circular imports
class BasicAuth(Auth):
    """Basic authentication class inheriting from Auth"""


    def __init__(self):
        # Import Auth here, inside the constructor, to avoid circular imports
        from api.v1.auth.auth import Auth
        self.auth = Auth()
