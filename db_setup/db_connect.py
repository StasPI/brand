import asyncio
import asyncpg
import yaml
from settings import config

class EngineDB():
    ''' подключение к бд с передачей запроса в экземпляр класса'''
    def __init__(self):
        pass

    async def run(self, command):
        conn = await asyncpg.connect(user=config['postgres']['user'],
                                     password=config['postgres']['password'],
                                     database=config['postgres']['database'],
                                     host=config['postgres']['host'],
                                     port=config['postgres']['port'])
        values = await conn.fetch(command)
        await conn.close()
        return values
