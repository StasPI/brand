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

    async def verification (self, user_pass):
        conn = await asyncpg.connect(user=self.user,
                                     password=self.password,
                                     database=self.database,
                                     host=self.host,
                                     port=self.port)
        values = await conn.fetchval('select name from brand where name = $1', user_pass)
        await conn.close()
        return values


connect = db_engine()
user_pass = '7fd80-29aff'

a = asyncio.get_event_loop().run_until_complete(connect.verification(user_pass))
print(a)
