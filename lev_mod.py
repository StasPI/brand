import json
import asyncio
from db_setup.db_connect import EngineDB
''' data '''
with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)
# ''' acync brand db '''
# comm = '''SELECT name FROM brand'''
# cursor = EngineDB().run(comm)
# loop = asyncio.get_event_loop()
# brand = loop.run_until_complete(cursor)

''' fuzzywuzzy'''
from fuzzywuzzy import fuzz


def fw(json_data):
    data = tuple(json_data['data'])
    brand = tuple(json_data['brand'])
        
    for row_data in data:
        for row_brand in brand:
            brand_name = row_brand[0].lower() #0 - Позиция имени бренда
            description = row_data[1].lower() #1 - Позиция описания/наменклатуры
            
            if brand_name in description.split():
                row_data.append('')
            elif fuzz.partial_ratio(description, brand_name) == 100:
                row_data.append('')


''' profiler '''
import cProfile

cProfile.run('fw(json_data)')

'188823310 function calls in 270.195 seconds'