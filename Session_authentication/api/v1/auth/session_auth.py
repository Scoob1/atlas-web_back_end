#!/usr/bin/env python3
""" Session Authentication Module """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session-based authentication """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a given user ID."""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns the User ID based on a given session ID."""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
