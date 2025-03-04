#!/usr/bin/env python3
""" New view for session authentication """
from flask import request, jsonify, make_response
from api.v1.auth.session_auth import SessionAuth
from models.user import User
import uuid

from api.v1.app import app


auth = SessionAuth()

@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Handle login requests """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(auth.SESSION_NAME, session_id)

    return response
