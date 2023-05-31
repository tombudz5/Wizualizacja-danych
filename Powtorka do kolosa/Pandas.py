import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('pokemon_data.csv', delimiter=',')
df = pd.read_csv('games.txt', delimiter=',')

# print(df.head(3))
# print(df.tail(3))

# READING COLUMNS
# print(df.columns)
# print(df[['Name', 'Type 1', 'HP']])

# READING ROWS
# print(df.iloc[0:4])
# print(df.iloc[2, 1])

# for index, row in df.iterrows():
#     print(index, row)

# print(df.loc[df['Type 1'] == 'Fire'])
# print(df.sample())
# print(df[(df['Price'] < '9.99') & (df['Price'] != 'Free')]['Price'])
# print(df[df.index.isin(['Minecraft'])])
# print(df.sort_values(['Game', 'Release Year'], ascending=[True, False]))

# df = df.drop(columns=['Total'])
# df['Total'] = df.iloc[:, 5].sum(axis=0)
# print(df['Total'])

# print(df)
# df[['Game', 'Release Year']].hist()
# df.plot.scatter(x='Game', y='Release Year')
# df.plot(x='Game', y='Release Year', kind='scatter') # kind= ['box', 'hexbin', 'pie', 'line', 'scatter']
# df['Release Year'].plot.kde()
plt.show()
















# #zad1,2
# plik = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(plik, header=0)
#
# print(df[df.Liczba > 1000])
# print('')
# print(df[df.Imie == 'RADOSŁAW'])
# print('')
# print(df.Liczba.sum())
# print('')
# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())
# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# print('')
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
#
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# # print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])

#zad3

# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df)
# print(df['Sprzedawca'].unique())
# print('')
# print(df.sort_values('Utarg', ascending=False).head(5))
# print('')
# print(df.groupby('Sprzedawca').size())
# print('')
# print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
# print(df.groupby('Kraj').size())
# print('')
# print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
#       agg({'Utarg': ['sum']}))
# print('')
# print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
# rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
# rok_2004.to_csv("zamowienia_2004.csv", index=False)


