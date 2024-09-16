#!/usr/bin/env python3
"""User module, creates a user class,
   inherits from Base and creates a table
   in the database called users
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """Representation of a user
        inherits from Base
            links to users table
            has, id, email,
            hashed_password,
            session_id, reset_token
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
