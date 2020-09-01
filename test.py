from queue import Queue
from threading import Thread
import csv
import json
import requests
q = Queue()
n_threads = 2
 
''' ''' 
FILENAME = r"A:\task\brand.csv"
brand_list = []
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        brand_list.append(row)
brand_list =  json.dumps(brand_list, ensure_ascii=False)      
''' '''
FILENAME = r"A:\task\prod.csv"
data_list = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 100000:
            count += 1
            data_list.append(row[:-1])
data_list = json.dumps(data_list, ensure_ascii=False)           
''' '''
data_list1 = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 5:
            count += 1
            data_list1.append(row[:-1])
data_list1 = json.dumps(data_list1, ensure_ascii=False)            
''' '''
ip = json.dumps('primer', ensure_ascii=False)
        
payload = {
    "brand": brand_list,
    "data": data_list,
    'ip': 'primer'
}
payload1 = {
    "brand": brand_list,
    "data": data_list1,
    'ip': 'da'
}



# r = requests.post("http://localhost:8080/find", data=payload)

# # r = requests.get(f'http://127.0.0.1:8000/brand/{payload}')
# print(r.text[1:200])
# print(r.json)


def download():
    global q
    pay = q.get()
    r = requests.post("http://localhost:8080/find", data=pay)
    print(r.text[1:200])
    print(r.json)
    q.task_done()

if __name__ == "__main__":
    pays = [
        payload1,
        payload,
    ]
    # fill the queue with all the urls
    for pay in pays:
        q.put(pay)
    # start the threads
    for t in range(n_threads):
        worker = Thread(target=download)
        # daemon thread means a thread that will end when the main thread ends
        worker.daemon = True
        worker.start()
    # wait until the queue is empty
    q.join()