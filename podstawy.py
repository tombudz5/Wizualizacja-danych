# lista = [6, 2, 3, 4, 5, 2, 3]
#
# lista.insert(2, 55) # dodanie elementu na danym miejscu
# print(lista)
# del lista[2] # usuwanie elementu po indexie, jezeli nie podamy indexu to usunie cala liste
# print(lista)
# lista.remove(2) # usuwa pierwszy napotkany element o danej wartosci
# print(lista)
# lista.extend([11, 22, 33]) # dodawanie paru wartosci na raz
# print(lista)
# lista.reverse() # odwraca liste
# print(lista)
# lista.sort() # sortuje liste
# print(lista)
# lista.pop(6) # usuwaniei elementy po indexie, jezeli nie ma podanego indexu to ostatni element
# print(lista)

slownik  = {1: "a", 2: 2, 3: [1, 2, 3], 4: "napis"}
print(slownik)
print(slownik[1])
slownik[5] = "drugi napis"
print(slownik)

slownik.pop(2)
print(slownik)
del slownik[3]

print(slownik.keys())
print(slownik.values())

print("a = %(zmienna)d" % {"zmienna": 12}) # inny zapis wyswietlania zmiennych
print("a = {}".format(12)) # jeszcze kolejny zapis


