import csv
import json
import requests

''' '''
file_brand = r"A:\git\brand\task\brand.csv"
brand_list = []
with open(file_brand, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        brand_list.append(row)

brand_list = json.dumps(brand_list, ensure_ascii=False)
''' '''
file_prod = r"A:\git\brand\task\prod.csv"
data_list = []
with open(file_prod, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        data_list.append(row[:-1])

data_list = json.dumps(data_list, ensure_ascii=False)
''' '''
ip = json.dumps('primer', ensure_ascii=False)

payload = {
    "brand": brand_list,
    "data": data_list,
    'ip': 'primer'
}
''' '''
r = requests.post("http://localhost:8080/find", data=payload)

print(r.json)
data = json.loads(r.text)
first_row = ['seller', 'name_of_product', 'id',
     'exact_match_brand', 'probable_match_brand', 'status']
data.insert(0, first_row)
''' '''

 

myFile = open(r"A:\git\brand\task\itogo.csv", 'w')
with myFile:
    writer = csv.writer(myFile, lineterminator='\n')
    writer.writerows(data)