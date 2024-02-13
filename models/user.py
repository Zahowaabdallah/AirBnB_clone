#!/usr/bin/python3

"""
this class define the user's attributes and methods
"""
import sys
import os
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """
        this method gets executed every time a new object is create
        """
        super().__init__(*args, **kwargs)
        self.email = ''  # single quotes indicating empty string
        self.password = ''
        self.first_name = ''
        self.last_name = ''

    def __str__(self):
        """
        str method for the user class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
