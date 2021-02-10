import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)


tasks = r.json()

for task in tasks:
    for key in task:
        if (len(key) < 8):
            print(key,'\t\t' ,task[key])
        else:
            print(key,'\t' ,task[key])
    print()
