import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

listaZeStrony = r.json()

def kto_zrobil_ile_zadan(lista):
    ktoZrobilIleZadan = {}
    for slownik in lista:
       if (slownik["completed"] == True):
            try:
                ktoZrobilIleZadan[slownik["userId"]] += 1
            except:
                ktoZrobilIleZadan[slownik["userId"]] = 1
    return ktoZrobilIleZadan



def rekord_zrobionych_zadan(jakaFunc, skad_lista):
    return max(jakaFunc(skad_lista).values())


def najlepsi_uzytkownicy(skad_lista):
    najlepsiUzytkownicy = []
    for uzytkownik, ileZadanWykonal in kto_zrobil_ile_zadan(skad_lista).items():
        if rekord_zrobionych_zadan(kto_zrobil_ile_zadan, skad_lista) == ileZadanWykonal:
            najlepsiUzytkownicy.append(uzytkownik)
    return najlepsiUzytkownicy

print(najlepsi_uzytkownicy(listaZeStrony))
        


