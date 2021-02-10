import requests

lista = []

with open("plik_szefa.txt", "r", encoding = "UTF-8") as file:
    for adres in file:
        lista.append(adres.replace("\n",""))
   
with open("dzialajaceStrony.txt", "w", encoding = "UTF-8") as file:
    for strona in lista:
        r = requests.get(strona)
        if(r.status_code == 200):
            file.write(strona + "\n")
    
