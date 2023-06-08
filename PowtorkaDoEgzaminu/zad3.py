import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('wynagrodzenia21.csv', delimiter=';', decimal=',')

new_df = pd.melt(df, id_vars=["Województwo"], var_name="Rok", value_name="Wynagrodzenie")

lata = np.arange(2010, 2014)
wynagrodzenia_kujawskopomorskie = [new_df.loc[(new_df['Rok'] == str(rok)) & (new_df['Województwo'] == 'KUJAWSKO-POMORSKIE'), 'Wynagrodzenie'].values[0] for rok in lata]
wynagrodzenia_lubelskie = [new_df.loc[(new_df['Rok'] == str(rok)) & (new_df['Województwo'] == 'LUBELSKIE'), 'Wynagrodzenie'].values[0] for rok in lata]
print(lata)
print(wynagrodzenia_kujawskopomorskie)
print(wynagrodzenia_lubelskie)

indeksy = np.arange(len(lata))

szerokosc_slupka = 0.35


fig, ax = plt.subplots()

wykres_kujawskopomorskie = ax.bar(indeksy, wynagrodzenia_kujawskopomorskie, szerokosc_slupka, label='Kujawsko-Pomorskie')
wykres_lubelskie = ax.bar(indeksy + szerokosc_slupka, wynagrodzenia_lubelskie, szerokosc_slupka, label='Lubelskie')

ax.set_xlabel('Lata')
ax.set_ylabel('Wynagrodzenie')
ax.set_title('Wykresy wynagrodzeń')

plt.text(0.30, 0.92, 'Tomasz Budzejko', transform=ax.transAxes, ha='right', va='bottom')

ax.set_xticks(indeksy + szerokosc_slupka / 2)
ax.set_xticklabels(lata)

ax.bar_label(wykres_kujawskopomorskie, fontsize=7)
ax.bar_label(wykres_lubelskie, fontsize=7)

ax.legend(loc='lower right')

plt.savefig('zad3.webp')

plt.show()






