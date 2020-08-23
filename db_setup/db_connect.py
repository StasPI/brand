import asyncio
import asyncpg
import yaml

with open('config.yaml') as read_file:
    conf = yaml.safe_load(read_file)


class EngineDB():
    ''' подключение к бд с передачей запроса в экземпляр класса'''
    def __init__(self):
        pass

    async def run(self, command):
        conn = await asyncpg.connect(user=conf['user'],
                                     password=conf['password'],
                                     database=conf['database'],
                                     host=conf['host'],
                                     port=conf['port'])
        values = await conn.fetch(command)
        await conn.close()
        return values
