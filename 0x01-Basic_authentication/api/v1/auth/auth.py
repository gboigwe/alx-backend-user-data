#!/usr/bin/env python3
"""The Module for Authentication"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Management of the Class API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The Method of validation if endpoint requires authentication"""

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        len_path = len(path)
        if len_path == 0:
            return True

        slash_path = True if path[len_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            len_exe = len(exc)
            if len_exe == 0:
                continue

            if exc[len_exe - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:len_exe - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
