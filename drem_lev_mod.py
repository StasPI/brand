import json
''' data '''
with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)

''' fuzzywuzzy'''
from fuzzywuzzy import fuzz


def fw(json_data):
    data = tuple(json_data['data'])
    brand = tuple(json_data['brand'])
        
    for row_data in data:
        for row_brand in brand:
            row_data_len = len(row_data)
            if row_data_len < 2:
                pass
            else:
                if row_data_len == 2:
                    brand_name = row_brand[0].lower() #0 - Позиция имени бренда
                    description = row_data[1].lower() #1 - Позиция описания/наменклатуры

                    if len(row_data) == 2:
                        if brand_name in description.split():
                            row_data.append('')
                        elif fuzz.partial_ratio(description, brand_name) == 100:
                            row_data.append('')


''' profiler '''
import cProfile

cProfile.run('fw(json_data)')