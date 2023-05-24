import numpy as np
import matplotlib.pyplot as mpl
import pandas as pd
import seaborn as sns
from PIL import Image

# WYKRESY Z POPRZEDNIEGO WYKŁADU KTÓRYCH NIE POKAZAŁ

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['wartości'])
# print(df)
# df['średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# mpl.legend()
# mpl.show()

# x = np.random.randn(10000)
# mpl.hist(x, bins=100, facecolor='y', alpha=0.8, density=True)
# mpl.xlabel('Wartości')
# mpl.ylabel('Prawdopodobieństwo')
# mpl.title('Histogram')
# mpl.grid()
# mpl.show()

# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext = mpl.pie(x=seria, labels=seria.index, autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), colors=['yellow', 'green'])
# mpl.title('Suma zamówień dla sprzedawców')
# mpl.legend(loc='lower right')
# mpl.ylabel('Procentowy wynik wartości zamówienia')
# mpl.show()

# SEABORN

# wykres liniowy
# sns.set(rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],label='linia nr1', color='yellow', marker='o', linestyle='-')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17],label='linia nr2', color='black', marker='^', linestyle='-')
# mpl.xlabel('oś x')
# mpl.ylabel('oś y')
# mpl.title('Wykres liniowy')
# mpl.show()


data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],'Populacja': [11190846, 1303171035, 207847528, 386754670]}
df = pd.DataFrame(data)
sns.set()
plot = sns.barplot(data=df, x='Kontynent', y='Populacja', ci=None, hue='Kontynent', estimator=np.sum, dodge=False, palette=['yellow', 'red', 'blue'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
mpl.show()
