# from db_setup.db_connect import db_connect
from config.settings import config
import asyncio
import asyncpg

user = config['postgres']['user']
password = config['postgres']['password']
database = config['postgres']['database']
host = config['postgres']['host']
port = config['postgres']['port']


class db_engine():
    ''' подключение к бд с передачей запроса в экземпляр класса'''
    def __init__(self,
                 user=user,
                 password=password,
                 database=database,
                 host=host,
                 port=port):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    async def connect(self, command):
        conn = await asyncpg.connect(user=self.user,
                                     password=self.password,
                                     database=self.database,
                                     host=self.host,
                                     port=self.port)
        values = await conn.fetchval(command)
        await conn.close()
        return values
    
    async def in_pass(self, pass):
        value = await self.connect(command)
        return value


connect = db_engine()
a = connect.in_pass(fr''' select name from brand where name = '7fd80-29aff' ''')

loop = asyncio.get_event_loop()
b = loop.run_until_complete(a)
print(b)