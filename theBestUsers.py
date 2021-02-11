import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

downloadList = r.json()

def how_many_true(list_, key, keyWithBoolean):
    dictionary ={}
    for record in list_:
        if record[keyWithBoolean] == True:
            try:
                dictionary[record[key]] += 1
            except:
                dictionary[record[key]] = 1
    return dictionary

userIdWithPoints = how_many_true(downloadList, "userId", "completed")

def keys_with_top_values(dictionary):
    list_ = []
    maxValue = max(dictionary.values())
    for key, value in dictionary.items():
        if(value == maxValue):
            list_.append(key)
    return list_

userIdWithPoints = how_many_true(downloadList, "userId", "completed")

theBestUsers = keys_with_top_values(userIdWithPoints)

print(theBestUsers)


            

