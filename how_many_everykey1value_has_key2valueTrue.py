import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

downloadList = r.json()

def how_many_everykey1value_has_key2valueTrue(lista, key1, key2):
    results ={}
    for slownik in lista:
        if slownik[key2] == True:
            try:
                results[slownik[key1]] += 1
            except:
                results[slownik[key1]] = 1
    return results

p = how_many_everykey1value_has_key2valueTrue(downloadList, "userId", "completed")

print(p)

