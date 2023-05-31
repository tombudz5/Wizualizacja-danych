import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_excel('imiona.xlsx')

print(df)
print(df[df['Plec'] == 'M'].groupby(by='Plec').count())
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),ascending=False).iloc[0])
