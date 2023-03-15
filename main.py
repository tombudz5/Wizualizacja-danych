import random
import math

#ZADANIE 1

# A = [1-x for x in range(0, 11)]
# print(A)
# B = [4**x for x in range(0, 8)]
# print(B)
# C = [x for x in B if x % 2 == 0]
# print(C)

#ZADANIE 2

# lista1 = list()
# i = 0
# while (i < 10):
#     liczba = random.randint(0, 1000)
#     lista1.append(liczba)
#     i += 1
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)

#ZADANIE 3

# produkty = {
#     "jablka": "szt",
#     "mieso": "kg",
#     "jogurt": "szt",
#     "orzechy": "gr"
# }
#
# nowa_lista = [produkt for produkt in produkty if produkty[produkt] == "szt"]
# print(nowa_lista)

#ZADANIE 4

# def czy_prostokatny(a, b, c):
#     if a ** 2 + b ** 2 == c ** 2:
#         return True
#     elif a ** 2 + c ** 2 == b ** 2:
#         return True
#     elif b ** 2 + c ** 2 == a ** 2:
#         return True
#     return False
#
# a = 3
# b = 4
# c = 6
#
# print(f"Czy trojkat o bokach rownych: a = {a} b = {b} c = {c} jest prostokatny? {czy_prostokatny(b, a, c)}")

#ZADANIE 5

# def pole_trapezu(a = 1, b = 1, h = 1):
#     pole = ((a+b) * h) / 2
#     return pole
#
# print(f"Pole trapezu wynosi: {pole_trapezu(2, 3, 4)}")

#ZADANIE 6

# def iloczyn_ciagu(a = 1, b = 4, ile = 10):
#     for i in range(a, a+10):
#         print(i * b)
#
# iloczyn_ciagu()

#ZADANIE 7

# def iloczyn_ciagu(a = 1, b = 4, ile = 10):
#     for i in range(a, a+10):
#         print(i * b)
#
# iloczyn_ciagu()

#ZADANIE 8

# def oblicz(**zakupy):
#     liczba_produktow = len(zakupy)
#     koszt = sum(zakupy.values())
#     print(liczba_produktow)
#     print(koszt)
#
#
# lista_zakupow = {
#     "jablka": 3.23,
#     "mieso": 16.29,
#     "jogurt": 3.12,
#     "orzechy": 7.97
# }
#
# oblicz(**lista_zakupow)

#ZADANIE 9

# liczba = int(input("Podaj liczbe: "))
#
# try:
#     pierwiastek = math.sqrt(liczba)
# except ValueError:
#     print("Musisz podac liczbe nieujemna!")
#     exit()
#
# print(pierwiastek)




