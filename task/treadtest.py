from queue import Queue
from threading import Thread
import csv
import json
import requests
q = Queue()
n_threads = 10
 
''' ''' 
FILENAME = r"A:\git\brand\task\brand.csv"
brand_list = []
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        brand_list.append(row)
brand_list =  json.dumps(brand_list, ensure_ascii=False)      
''' '''
FILENAME = r"A:\git\brand\task\prod.csv"
data_list = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 10:
            count += 1
            data_list.append(row[:-1])
data_list = json.dumps(data_list, ensure_ascii=False)           
''' '''
data_list1 = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 1000:
            count += 1
            data_list1.append(row[:-1])
data_list1 = json.dumps(data_list1, ensure_ascii=False)            
''' '''
data_list2 = []
with open(FILENAME, "r", newline="") as file:
    count = 0
    reader = csv.reader(file)
    for row in reader:
        if count != 1000:
            count += 1
            data_list2.append(row[:-1])
data_list2 = json.dumps(data_list2, ensure_ascii=False)   
''' '''
ip = json.dumps('primer', ensure_ascii=False)
        
payload = {
    "brand": brand_list,
    "data": data_list,
    'token': ip
}
payload1 = {
    "brand": brand_list,
    "data": data_list1,
    'token': ip
}
payload2 = {
    "brand": brand_list,
    "data": data_list2,
    'token': ip
}




# r = requests.post("http://localhost:8080/find", data=payload)
# # r = requests.get("http://localhost:8080/")

# print(len(r.text))
# print(r.json)

ct = 0
def download():
    global q
    global ct
    pay = q.get()
    r = requests.post("http://localhost:8080/find", data=pay)
    # print(r.text[1:200])
    print(r.json)
    ct += 1
    print(ct)
    print(r.text[1:300])
    q.task_done()

if __name__ == "__main__":
    pays = [
        payload1,
        payload,
        payload2,
        payload1,
        payload,
        payload2,
        payload2,
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