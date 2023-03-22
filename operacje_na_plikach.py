# #ZADANIE 1
#
# file = open("zadanie1.txt", "a+");
#
# for i in range(0, 31):
#     liczba = i * 2
#     file.write(str(liczba) + "\n")


# #ZADANIE 2
#
# file = open("zadanie1.txt", "r")
#
# for line in file.readlines():
#     print(line.strip())


# #ZADANIE 3
#
# with open("zadanie3.txt", "w") as file:
#     file.write("""pierwsza linia
# druga linia
# trzecia linia
# czwarta linia
#     """)
#
# with open("zadanie3.txt", "r") as f:
#     for line in f.readlines():
#         print(line.strip())


# #ZADANIE 4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu)
#     def ile_produktu(self):
#         print(str(self.ilosc) + self.jednostka_miary)
#     def ile_kosztuje(self):
#         print(self.ilosc * float(self.cena_jed))
#
#
# nowy_obiekt = NaZakupy("Banan", 5, "kg", "2.35")
# nowy_obiekt.wyswietl_produkt()
# nowy_obiekt.ile_produktu()
# nowy_obiekt.ile_kosztuje()


# # ZADANIE 5
# class CiagArytmetyczny:
#     def __init__(self, wartosci):
#         self.wartosci = wartosci
#
#     def wyswietl_dane(self):
#         for wartosc in self.wartosci:
#             print(wartosc)
#
#     def pobierz_elementy(self, pocz_zakresu, koniec_zakresu):
#         if pocz_zakresu < 0 or koniec_zakresu > len(self.wartosci):
#             print("Taki zakres jest nieosiagalny")
#             return
#         for i in range(pocz_zakresu-1, koniec_zakresu):
#             print(self.wartosci[i])
#
#     def pobierz_parametry(self):
#         print(f"Pierwszy element: {self.wartosci[0]}")
#         print(f"Roznica: {self.wartosci[1] - self.wartosci[0]}")
#         print(f"Ostatni element: {self.wartosci[len(self.wartosci)-1]}")
#
#     def policz_sume(self):
#         suma = 0
#         for element in self.wartosci:
#             suma += element
#         print(suma)
#
#     def policz_elementy(self):
#         print(len(self.wartosci))
#
#
# ciag = CiagArytmetyczny([1, 3, 5, 7, 9, 11])
# ciag.wyswietl_dane()
# ciag.pobierz_elementy(2, 7)
# ciag.pobierz_parametry()
# ciag.policz_sume()
# ciag.policz_elementy()