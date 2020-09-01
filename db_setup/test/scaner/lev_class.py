import json
from multiprocessing import Pool, cpu_count

from rapidfuzz import fuzz
''' data '''

with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)
''' rapidfuzz'''


class BrandScanner():  
    # def __init__(self, brand, data):
    #     self.brand = brand
    #     self.data = data
    def __init__(self, json_data):
        self.json_data = json_data

    def retrieving_objects(self):
        # Принимает объект json, извлекает нужные данные с небольшим форматированием
        # Возвращает готовые к работе объекты описаний товаров и брендов
        # порядок подачи данных важен! 0 - название организации. 1 - наименование товара. 2 - id.
        # порядок подачи брендов важен! 0 - название бренда. 1 - id.
        data = tuple(self. json_data['data'])
        # 0 - Позиция имени бренда
        brand = tuple(brand_name[0].lower() for brand_name in self.json_data['brand'])
        return data, brand
    
    @staticmethod
    def fast_string_comparison(brand, product_name):
        # Принимает строчные списковые данные бренда и описания товара
        # Проверяет в лоб вхождение из списка брендов список слов в описании товара
        # Возвращает список с совпадениями и список без совпадений
        product_name = product_name.split()
        exact_match_brand = list(set(brand) & set(product_name))
        exclusive_matches_brand = tuple(set(brand) ^ set(exact_match_brand))
        return exact_match_brand, exclusive_matches_brand

    @staticmethod
    def status_brand(row_data):
        exactly = row_data[-2]
        not_exactly = row_data[-1]
        len_exactly = len(row_data[-2])
        len_not_exactly = len(row_data[-1])
        if exactly and not_exactly:        
            if len_exactly == 1 and len_not_exactly == 1:
                row_data.append('found but probably there is a match')
            elif len_exactly == 1 and len_not_exactly > 1:
                row_data.append('found but probably a couple of matches')
            elif len_exactly > 1 and len_not_exactly == 1:
                row_data.append('found several but probably there is a match')
            elif len_exactly > 1 and len_not_exactly > 1:
                row_data.append('found a few but probably a few matches')
        elif exactly:
            if len_exactly == 1:
                row_data.append('found')
            else:
                row_data.append('found several')
        elif not_exactly:
            if len_not_exactly == 1:
                row_data.append('probably found')
            else:
                row_data.append('probably found several')
        else:
            row_data.append('not found')
    
    # @staticmethod
    def handler(self, row_data):
        probable_match_brand = []
        # 1 - Позиция описания/наменклатуры
        product_name = row_data[1].lower()
        exact_match_brand, exclusive_matches_brand = self.fast_string_comparison(
            brand, product_name)
        for brand_name in exclusive_matches_brand:
            similarity_number = int(fuzz.partial_ratio(product_name, brand_name))
            if similarity_number >= 90:
                # все точные совпадения
                exact_match_brand.append(brand_name)
            elif 76 <= similarity_number <= 89:
                # все возможные совпадения
                probable_match_brand.append(brand_name)
        row_data.append(exact_match_brand)
        row_data.append(probable_match_brand)
        self.status_brand(row_data)
        return row_data

    # @staticmethod
    # def start(self):
    #     ''' processing '''
    #     if __name__ == '__main__':
    #         with Pool(8) as p:
    #             data = p.map(self.handler, self.data)
    #         return data
        
        
        

# def retrieving_objects(json_data):
#     # Принимает объект json, извлекает нужные данные с небольшим форматированием
#     # Возвращает готовые к работе объекты описаний товаров и брендов
#     # порядок подачи данных важен! 0 - название организации. 1 - наименование товара. 2 - id.
#     # порядок подачи брендов важен! 0 - название бренда. 1 - id.
#     data = tuple(json_data['data'])
#     # 0 - Позиция имени бренда
#     brand = tuple(brand_name[0].lower() for brand_name in json_data['brand'])
#     return data, brand



# data, brand = retrieving_objects(json_data)
# lev = BrandScanner(brand, data)

# ''' processing '''
# if __name__ == '__main__':
#     with Pool(8) as p:
#         data = p.map(lev.handler, data)
#     print(data[1])   

lev = BrandScanner(json_data)
data, brand = lev.retrieving_objects()
''' processing '''
if __name__ == '__main__':
    with Pool(8) as p:
        data = p.map(lev.handler, data)
    print(data[1])   