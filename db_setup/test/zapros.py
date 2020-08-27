import csv
import json

FILENAME = r"A:\task\prod.csv"
data_list = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 100000:
            count += 1
            data_list.append(row[:-1])

print(len(data_list))


FILENAME = r"A:\task\brand.csv"
brand_list = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        brand_list.append(row)

print(len(brand_list))






with open('test_file.json', 'w') as write_file:
    data = {
    "brand": brand_list,
    "data": data_list,
    'ip': 'primer'
    }
    json.dump(data, write_file, ensure_ascii=False)

with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)
    
print(len(json_data['data']))
print(len(json_data['brand']))
print(json_data['ip'])