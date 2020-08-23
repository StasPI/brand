import json
import asyncio
from db_setup.db_connect import EngineDB

''' data '''
with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)

data = json_data['data']

''' acync brand db '''
comm = '''SELECT name FROM brand'''
cursor = EngineDB().run(comm)
loop = asyncio.get_event_loop()
brand = loop.run_until_complete(cursor)
