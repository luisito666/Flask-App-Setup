"""
    Config Module
"""
import os

DEBUG = os.environ['DEBUG']

if DEBUG:
    from .dev import Config
else:
    from .prod import Config
