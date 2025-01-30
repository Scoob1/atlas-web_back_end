#!/usr/bin/env python3
"""
This module filters and obfuscates sensitive fields in log messages.

It provides a function `filter_datum` that
replaces specified fields with a redaction string.
"""

import logging
import re
from typing import List


# task 0.
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


# task 1
class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize with fields."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record."""
        message = record.getMessage()
        # Use filter_datum to redact the fields in the message
        message = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR
        )
        record.msg = message
        return super().format(record)
