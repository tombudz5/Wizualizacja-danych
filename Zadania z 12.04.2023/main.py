import numpy as np

# # inicjalizacja tablicy
# a = np.array([0, 1])
# print(a)
#
# # drugi sposob na stworzenie tablicy
# a = np.arange(2, 5, 1)  # od, do, co ile
# print(a)
#
# # wypisanie typu tablicy nie jej elementow
# print(type(a))
#
# # sprawdzenie typu danych tablicy
# print(a.dtype)
#
# # inicjalizacja tablicy z konkretnym typem danych
# a = np.arange(2, dtype="int64")
# print(a.dtype)  # dane w tablicy beda mialy typ 64 - bitowy
#
# a = np.array([[0, 1], [2, 3]])  # "macierze", kazda tablica w tej tablicy musi miec tyle samo elementow
# print(a)
# print(a.shape)  # ksztalt tablicy, wymiary macierzy
# print(a.ndim)  # wielkosc tablicy
#
# m = np.array([np.arange(2), np.arange(2)])  # stworzenie tablicy wielowymiarowej za pomoca arange
# print(m)
# print(m.shape)
# print(type(m))
#
# # kopia tablicy a, ale z innym typem danych
# b = a.astype("float")
# print(b)
# print(type(b))
# print(b.dtype)  # w tym przypadku typ danych to float64
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((3, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)  # domyslny typ dla takich tablic to float64
# print(jedynki.dtype)  # domyslny typ dla takich tablic to float64
#
# pusta = np.empty((2,2))
# print(pusta)

# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
# poz_1 = macierz[1, 1]  # pierwszy sposob, w jendym nawiasie najpierw wiesz, potem kolumna (liczac od 0)
# poz_2 = macierz[0][0]  # drugi sposob, tak samo tylko w oddzielnych nawiasach (oddzielne indeksy) (liczac od 0)
# print(poz_1)
# print(poz_2)

# liczby_lin = np.linspace(1, 2, 5, endpoint=False)  # wartosci pomiedzy 1, 2 i ma być tych wartosci 5 bez liczenia ostatniego elementu (bez 2)
# print(liczby_lin)
#
# liczby_lin = np.linspace(1, 2, 5)  # wartosci pomiedzy 1, 2 i ma być tych wartosci 5
# print(liczby_lin)

# z = np.indices((5,3))  # tworzy dwie macierze, pierwsza ktora jest inkrementowana kolumnami, druga wierszami
# print(z)  # wypisuje obie macierze
# print(z[0][1][2])  # [0] ktora z dwoch macierz, [1] ktory wiersz z tej macierzy, [2] ktory element z [1] wiersza

# mac_diag = np.diag([a for a in range(5)])
# print(mac_diag)

# mat_diag_k = np.diag([a for a in range(5)], 1)  # kazdy element na diagonali przesuniety o 1
# print(mat_diag_k)

# z = np.fromiter(range(5), dtype="int32")
# print(z)

# znaki = b"ogolna"
#
# z1 = np.frombuffer(znaki, dtype="S1")
# print(z1)
#
# znaki = "ogolna"
# z3 = np.array(list(znaki))
# print(z3)
# z4 = np.array(list(znaki), dtype="S1")
# print(z4)
# z5 = np.array(list(b"ogolna"))
# print(z5)
# z6 = np.fromiter(znaki, dtype = "S1")
# print(z6)

# # sposoby na ciecie tablicy
#
# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)  # to samo
# print(a[s])
#
# s = range(2, 7, 2)  # to samo
# print(a[s])
#
# print(a[2:7:2])  # inny sposob
#
# print(a[1:])  # jescze inny
# print(a[2:5])
