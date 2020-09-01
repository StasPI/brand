from queue import Queue
from threading import Thread
import csv
import json
import requests
# q = Queue()
# n_threads = 2
# buffer_size = 1024
 

FILENAME = r"A:\task\prod.csv"
data_list = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 5:
            count += 1
            data_list.append(row[:-1])

 
FILENAME = r"A:\task\brand.csv"
brand_list = []
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        brand_list.append(row)
        
        
brand_list =  json.dumps(brand_list, ensure_ascii=False)
data_list = json.dumps(data_list, ensure_ascii=False)
ip = json.dumps('primer', ensure_ascii=False)
        
payload = {
    "brand": brand_list,
    "data": data_list,
    'ip': 'primer'
}


# payload = {'mess': 'eg'}
json_data = json.dumps(payload, ensure_ascii=False)

# r = requests.get(f'http://127.0.0.1:8000/brand/{brand_list}')
r = requests.post("http://localhost:8080/find", data=payload)

# r = requests.get(f'http://127.0.0.1:8000/brand/{payload}')
print(r.text[1:200])
print(r.json)