#!/usr/bin/env python3
"""The session for the user module"""


from models.base import Base


class UserSession(Base):
    """The class for the user session"""

    def __init__(self, *args: list, **kwargs: dict):
        """Method to initialize the user session"""

        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
