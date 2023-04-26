import numpy as np

# # ZADANIE 1
#
# tablica = np.arange(0, 4*20, 4)
# print(tablica)

# # ZADANIE 2
#
# a = np.arange(5, dtype="float64")
#
# b = a.astype("int32")
#
# print(a.dtype)
# print(b.dtype)

# # ZADANIE 3
#
# def funkcja(n):
#     macierz = np.array([2**i for i in range(n**2)])
#     macierz = macierz.reshape((n, n))
#     return macierz
#
# print(funkcja(5))

# # ZADANIE 4
#
# def generuj(podstawa, liczba_poteg):
#     potegi = np.logspace(0, liczba_poteg - 1, num=liczba_poteg, base=podstawa)
#     return potegi
#
# print(generuj(2, 4))