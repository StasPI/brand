import json

from rapidfuzz import fuzz
'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Main processing module.
'''


class BrandScanner():
    ''' 
    Main processing class
    
    Uses direct validation first to avoid the overhead of a partial matching 
    algorithm.
    Then, all lines in which the required information was not found during 
    direct verification are sent for verification by the partial matching 
    algorithm.
    '''
    def __init__(self, brand, data):
        self.brand = brand
        self.data = data

    def retrieving_objects(self):
        # Accepts a json object, retrieves the data you want with a little formatting
        # Returns ready-to-use product and brand description objects
        # the order of data submission is important! 0 is the name of the organization.
        # 1 - product name. 2 - id.
        # brand submission order is important! 0 is the brand name. 1 - id.
        self.data = tuple(self.data)
        # 0 - Brand Name Position
        self.brand = tuple(brand_name[0].lower() for brand_name in self.brand)
        return self.data, self.brand

    @staticmethod
    def fast_string_comparison(brand, product_name):
        # Accepts inline listing brand data and product descriptions
        # Performs a direct check for entry from the list of brands list of words in 
        # the product description
        # Returns a list with matches and a list without matches
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

    def handler(self, row_data):
        probable_match_brand = []
        # 1 - Description / Nomenclature Position
        product_name = row_data[1].lower()
        exact_match_brand, exclusive_matches_brand = self.fast_string_comparison(
            self.brand, product_name)
        for brand_name in exclusive_matches_brand:
            similarity_number = int(
                fuzz.partial_ratio(product_name, brand_name))
            if similarity_number >= 90:
                # All exact matches
                exact_match_brand.append(brand_name)
            elif 76 <= similarity_number <= 89:
                # All possible matches
                probable_match_brand.append(brand_name)
        row_data.append(exact_match_brand)
        row_data.append(probable_match_brand)
        self.status_brand(row_data)
        return row_data
