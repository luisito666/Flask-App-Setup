"""
    Config Module
"""
import os

DEBUG = int(os.environ['DEBUG'])

if DEBUG:
    from .dev import Config
else:
    from .prod import Config
