#!/usr/bin/env python3
"""
Module contains functions to encrypt password
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a randomly generated salt using bcrypt.
    :param password: The plain text password to hash.
    :return: The salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a given hashed password.
    :param hashed_password: The hashed password.
    :param password: The plain text password to verify.
    :return: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
