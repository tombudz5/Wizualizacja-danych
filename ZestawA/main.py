import math

# # ZADANIE 1
#
# a = input("a = ")
# b = input("b = ")
#
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     print("Musisz podac liczby calkowite")
#     exit()
#
# wynik = (a**2) + (a * b) + (b**2)
#
# file = open("zadanie1.txt", "w", encoding="utf-8")
# file.write(f"a^2 + ab + b^2 = {a}^2 + {a}*{b} + {b}^2 = {str(wynik)}")
# file.close()

# # ZADANIE 2
#
# def suma_list(l1, l2):
#     nowa_lista = []
#     if len(l1) > len(l2):
#         for i in range(0, len(l1)):
#             try:
#                 nowa_lista.append(l1[i] + l2[i])
#             except IndexError:
#                 nowa_lista.append(l1[i] + 0)
#     else:
#         for i in range(0, len(l2)):
#             try:
#                 nowa_lista.append(l1[i] + l2[i])
#             except IndexError:
#                 nowa_lista.append(0 + l2[i])
#     return nowa_lista
#
#
# lista1 = [5, 2, -1, 4, 33]
# lista2 = [1, 2, 5, 3, 4, 21, 3]
#
# print(suma_list(lista1, lista2))


# # ZADANIE 3
#
# with open("tekst.txt", "r", encoding="UTF-8") as file:
#     file.seek(100)
#     znaki = file.read(35)
#
# count = 0
#
# for znak in znaki:
#     if znak.isupper():
#         print(znak)
#         count += 1
#
# if count <= 0:
#     print("Nie ma wielkich liter")
#     exit()
#
# print("Liczba wielkich liter: " + str(count))


# # ZADANIE 4
#
# lista = [1, 2, 5, 6, 3, 5, 7, 7, 8, 2]
# a = 2
#
# nowa_lista = [el for el in lista if el > a]
# print(nowa_lista)

# ZADANIE 5

wynik = ((math.e**3) + (math.cos(39)**2))**(1/5) + (2/7)**3 + math.pi
print(round(wynik, 2))