#!/usr/bin/env python3


"""The Module for the filter_datum function for log obfuscation.
"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): List of strings representing fields to obfuscate.
        redaction (str): String to replace sensitive information.
        message (str): Log line to obfuscate.
        separator (str): Character separating fields in the log line.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = rf'({"|".join(map(re.escape, fields))})\{separator}[^{separator}]+'
    return re.sub(pattern, f'\\1{separator}{redaction}', message)
