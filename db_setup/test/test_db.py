"""
Module that implements the connection to the database.

You need to provide data to access an empty database.
"""

import asyncio
import asyncpg
import csv

create_brand = '''CREATE TABLE brand
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
); '''


async def run():
    type_db = 'postgresql'
    user_name_db = 'postgres'
    password_db = 'testpass'
    host_db = 'localhost'
    port_db = '5432'
    name_db = 'lev'

    conn = await asyncpg.connect(
        f'{type_db}://{user_name_db}:{password_db}@{host_db}:{port_db}/{name_db}'
    )
    
    values = await conn.fetch(create_brand)
    FILENAME = r"A:\task\brand.csv"
    with open(FILENAME, "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[1], row[0])
            values = await conn.fetch(f'''insert into brand (id, name) values ({row[1]}, $anystring$'{row[0]}'$anystring$)''')
 
    await conn.close()


loop = asyncio.get_event_loop()  
loop.run_until_complete(run())