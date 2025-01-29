#!/usr/bin/env python3
"""
This module filters and obfuscates sensitive fields in log messages.

It provides a function `filter_datum` that replaces specified fields with a redaction string.
"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in the log message.

    Arguments:
    fields: list of fields to obfuscate.
    redaction: the string to replace the field values.
    message: the log message to modify.
    separator: character separating the fields.

    Returns:
    The modified log message with obfuscated fields.
    """
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]+',
                         f'{field}={redaction}', message)
    return message
