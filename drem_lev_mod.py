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


''' fuzzywuzzy'''
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

test_list = []

def eva(x, y):
    return fuzz.partial_ratio(x, y)

def fw():
    count = 0
    for i in data:
        if 'durex'.lower() in i[1].lower().split():
            count += 1
        elif eva(i[1], 'durex' ) == 100:
            count += 1
    print(count)


''' profiler '''
import cProfile

cProfile.run('fw()')
