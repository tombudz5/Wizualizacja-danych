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

# slownik  = {1: "a", 2: 2, 3: [1, 2, 3], 4: "napis"}
# print(slownik)
# print(slownik[1])
# slownik[5] = "drugi napis"
# print(slownik)
#
# slownik.pop(2)
# print(slownik)
# del slownik[3]
#
# print(slownik.keys())
# print(slownik.values())
#
# print("a = %(zmienna)d" % {"zmienna": 12}) # inny zapis wyswietlania zmiennych
# print("a = {}".format(12)) # jeszcze kolejny zapis


# napis = input("wpisz cos: ") # wczytywanie input od uzytkownika
#
# print(napis)

# a = int(input("Podaj pierwsza liczbe: "))
# b = int(input("Podaj druga liczbe: "))
#
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a = b")

# a = int(input("Podaj pierwsza liczbe: "))
# b = int(input("Podaj druga liczbe: "))
#
# if a == b:
#     print("a = b")
# else:
#     print("a != b")

# a = int(input("Podaj pierwsza liczbe: "))
# b = int(input("Podaj druga liczbe: "))
# c = int(input("Podaj trzecia liczbe: "))
# d = int(input("Podaj czwarta liczbe: "))

# trzy sposoby zapisania warunku z "i"

# if (a > b) and (c < d):
#     print("a > b i c < d")
#
# if a > b and c < d:
#     print("a > b i c < d")

# if a > b & c < d:
#     print("a > b i c < d")

# if (a > b) | (c < d): # musza byc nawiasy inaczej nie zadziała poprawnie
#     print("a > b albo c < d")

# if (a > b) or (c < d):
#     print("a > b albo c < d")

# lista = [6, 2, 3, 4, 5, 2, 3]
# output = ""
#
# for i in range(0, len(lista)):
#     output += str(lista[i]) + " "
# print(output)
#
# output = ""
# for liczba in lista:
#     output += str(liczba) + " "
# print(output)

# lista = [6, 2, 3, 4, 5, 2, 3]
#
# licznik = 0
#
# while licznik != len(lista):
#     print(f"{licznik}: {lista[licznik]}")
#     licznik += 1




