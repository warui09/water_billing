#!/usr/bin/python3

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "long_string_hard_to_guess"
