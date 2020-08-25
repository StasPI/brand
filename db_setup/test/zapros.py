import csv
import json

FILENAME = r"A:\task\prod.csv"

data_list = []
with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        data_list.append(row[:-1])

with open('test_file.json', 'w') as write_file:
    data = {
    "data": data_list,
    'ip': 'primer'
    }
    json.dump(data, write_file, ensure_ascii=False)

with open('test_file.json', 'r') as read_file:
    json_data = json.load(read_file)
    
print(len(json_data['data']))
print(json_data['ip'])