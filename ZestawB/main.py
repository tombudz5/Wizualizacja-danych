import math

# # ZADANIE 1
#
# with open("tekst.txt", "r", encoding="UTF-8") as file:
#     file.seek(71)
#     znaki = file.read(40)
#
# if znaki.count('A') <= 0:
#     print("Nie ma liter A")
# else:
#     print(f"Liczba liter A: {znaki.count('A')}")


# # ZADANIE 2
#
# lista = [2, 3.12, 3.14, 123, 12, 2.112, 10.23]
# nowa_lista = [el for el in lista if type(el) == float]
#
# print(lista)
# print(nowa_lista)

# # ZADANIE 3
#
# def suma(l):
#     liczba_iteracji = len(l)
#     pierwszy_el = l[0]
#     for i in range(1, liczba_iteracji):
#         l.append(pierwszy_el + l[i])
#     return l
#
# lista = [2, 5, 3, 3.14, 52.3, 6, 5.23, 8]
# print(lista)
# print(suma(lista))

# # ZADANIE 4
#
# wynik = math.sin(56)**2 + ((4**2/25) + math.log(85, 3))**(1/4)
# print(wynik)

# # ZADANIE 5
#
# n = input("Podaj liczbe calkowita n: ")
#
# try:
#     n = int(n)
# except ValueError:
#     print("Musisz podac liczbe calkowita!")
#
# suma = 0
#
# for i in range(1, n+1):
#     suma += i
#
# file = open("zadanie5.txt", "w")
#
# file.write(str(suma))
# file.close()
