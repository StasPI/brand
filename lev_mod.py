import json
from multiprocessing import Pool

from rapidfuzz import fuzz

''' data '''

with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)
''' rapidfuzz'''


def retrieving_objects(json_data):
    # Принимает объект json, извлекает нужные данные с небольшим форматированием
    # Возвращает готовые к работе объекты описаний товаров и брендов
    data = tuple(json_data['data'])
    # 0 - Позиция имени бренда
    brand = tuple(brand_name[0].lower() for brand_name in json_data['brand'])
    return data, brand


def fast_string_comparison(brand, product_name):
    # Принимает строчные списковые данные бренда и описания товара
    # Проверяет в лоб вхождение из списка брендов список слов в описании товара
    # Возвращает список с совпадениями и список без совпадений
    product_name = product_name.split()
    exact_match_brand = list(set(brand) & set(product_name))
    exclusive_matches_brand = tuple(set(brand) ^ set(exact_match_brand))
    return exact_match_brand, exclusive_matches_brand


def handler(row_data):
    probable_match_brand = []
    # 1 - Позиция описания/наменклатуры
    product_name = row_data[1].lower()
    exact_match_brand, exclusive_matches_brand = fast_string_comparison(
        brand, product_name)
    for brand_name in exclusive_matches_brand:
        similarity_number = int(fuzz.partial_ratio(product_name, brand_name))
        if similarity_number >= 88:
            # все точные совпадения
            exact_match_brand.append(brand_name)
        elif 76 <= similarity_number <= 87:
            # все возможные совпадения
            probable_match_brand.append(brand_name)
    row_data.append(exact_match_brand)
    row_data.append(probable_match_brand)
    return row_data


data, brand = retrieving_objects(json_data)
''' processing '''
if __name__ == '__main__':
    with Pool(8) as p:
        data = p.map(handler, data)
        
        
"""

1 точно

2 точно несколько

3 точно возможно

4 возможно

5 возможно несколько

"""