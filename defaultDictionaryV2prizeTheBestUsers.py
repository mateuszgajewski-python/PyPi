import requests
import json
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")

downloadList = r.json()

def how_many_true(list_, key, keyWithBoolean):
    dictionary = defaultdict(int)               ################
    for record in list_:
        if record[keyWithBoolean] == True:
            dictionary[record[key]] += 1            
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

def tail_of_address_ampersand(myList, key = "id"):
    i = 1
    wynik = ""
    for x in myList:
        if(len(myList) == i):
            wynik += key + "=" + str(x)
        else:
            wynik += key + "=" + str(x) + "&"
        i += 1
        
    return wynik


#sposób 2
for theBestUser in theBestUsers:
    r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(theBestUser))
    user = r.json()
    print("Ciasteczko dostaje użytkownik o imieniu", user["name"])

#sposób 3
r = requests.get("https://jsonplaceholder.typicode.com/users?" + tail_of_address_ampersand(theBestUsers))
users = r.json()
for user in users:
    print ("Ciasteczko dostaje użytkownik o imieniu", user["name"])
