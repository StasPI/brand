"""
Module that implements the connection to the database.

You need to provide data to access an empty database.
"""

import asyncio
from sqlalchemy import create_engine
import yaml

with open('config.yaml') as f:
    templates = yaml.safe_load(f)


