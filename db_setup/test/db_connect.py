"""
Module that implements the connection to the database.

You need to provide data to access an empty database.
"""

import yaml
from sqlalchemy import create_engine

with open('config.yaml') as read_file:
    conf = yaml.safe_load(read_file)


class EngineDB():
    type_db = conf['type_db']
    driver = conf['driver']
    user = conf['user']
    password = conf['password']
    host = conf['host']
    port = conf['port']
    database = conf['database']

    # type_db = 'postgresql'
    # driver_db = 'psycopg2'
    # user_name_db = 'postgres'
    # password_db = 'testpass'
    # host_db = 'localhost'
    # port_db = '5432'
    # name_db = 'test_api_db'

    def __init__(self):
        pass

    def connect_db(self):
        return create_engine(
            f'{self.type_db}+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}',
            echo=True)
