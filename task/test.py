import csv
import ujson
import requests
from sys import getsizeof
import time

''' '''
file_brand = r"A:\git\brand\task\brand.csv"
brand_list = []
with open(file_brand, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        brand_list.append(row)

brand_list = ujson.dumps(brand_list, ensure_ascii=False)
''' '''
file_prod = r"A:\git\brand\task\prod.csv"
data_list = []
with open(file_prod, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 100000:
            count += 1
            data_list.append(row[:-1])
data_list = ujson.dumps(data_list, ensure_ascii=False)

''' '''
token = ujson.dumps('tok', ensure_ascii=False)


json_data = {
    "brand": brand_list,
    "data": data_list,
}

params = {
    "size": getsizeof(data_list),
    'token': token
}
''' '''

start_time = time.time()
r = requests.post("http://localhost:8080/find",params=params, data=json_data)
print("--- %s seconds ---" % (time.time() - start_time))
print(r.json)
print(r.text[1:400])