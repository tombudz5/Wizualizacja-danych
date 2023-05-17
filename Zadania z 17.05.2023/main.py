import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
from PIL import Image

# mpl.plot([1, 5, 10, 15, 20, 25, -10, 25, 20, 15, 10, 5, 1, 2, 3, 3, 2, 2])
# mpl.show()

# x = np.array([1,2, 3, 4])
# y = x**2
#
# mpl.plot(x, y, 'yo-')
# mpl.axis([0, 6, 0, 20])
# mpl.show()
#
# mpl.plot(x, y, 'r')
# mpl.plot(x, y, 'o')
# mpl.axis([0, 6, 0, 20])
# mpl.show()

# x = np.arange(0, 5, 0.2)
# mpl.plot(x, x, 'r-', label='liniowa')
# mpl.plot(x, x**2, 'b-',label='kwadratowa')
# mpl.plot(x, x**3, 'g-', label='szescienna')
# mpl.legend(loc='best')
# # mpl.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# mpl.show()

# x = np.arange(0, math.pi*10, 0.1)
# y = [math.sin(i) for i in x]
#
# mpl.plot(x, y, 'y-', label='sin(x)')
# mpl.legend(loc="center right")
# mpl.xlabel('wartosci x')
# mpl.ylabel('wartosci y')
# mpl.title('wykres funkcji sinus')
# mpl.show()


# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# mpl.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# mpl.xlabel('klucz a')
# mpl.ylabel('klucz b')
# mpl.show()

x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(x1 * np.pi * 2)
y2 = np.cos(x2 * np.pi * 2)
#
# mpl.subplot(4, 1, 1)
# mpl.plot(x1, y1, 'r-')
# mpl.title('Wykres sin(x)')
# mpl.xlabel('Wartosci x')
# mpl.ylabel('Wartosci y')
#
# mpl.subplot(4, 1, 4)
# mpl.plot(x2, y2, 'y-')
# mpl.title('Wykres cos(x)')
# mpl.xlabel('Wartosci x')
# mpl.ylabel('Wartosci y')
# mpl.subplots_adjust(hspace=0.5)
# mpl.show()

# fig, axs = mpl.subplots(3, 2)
# axs[0,0].plot(x1, y1)
# axs[0,0].set_title('wykres sin(x)')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('y')
#
# axs[1,1].plot(x2, y2)
# axs[1,1].set_title('wykres cos(x)')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('y')
#
# axs[2,0].plot(x1, y1, 'r')
# axs[2,0].set_title('wykres sin(x)')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('y')
#
# mpl.subplots_adjust(hspace=1, wspace=0.25)
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# mpl.show()


data = {'Kraj': ['Belgia', 'Polska', 'Niemcy', 'Tunezja', 'USA'],
        'Stolica': ['Bruksela', 'Warszawa', 'Berlin', 'Tunis', "Waszyngton"],
        'Kontynent': ['Europa', 'Europa', 'Europa', 'Afryka', 'Ameryka Polnocna'],
        'Populacja': [11190846, 39500000, 83000000, 32000000, 348000000]}

df = pd.DataFrame(data)
print(df)

# grupa = df.groupby('Kontynent')
#
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
#
# mpl.bar(x=etykiety,
#         height=wartosci,
#         color=['yellow', 'red', 'blue', 'green'])
#
# mpl.xlabel('Kontynenty')
# mpl.ylabel('Populacja')
#
# mpl.show()

grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
print(grupa)

# pierwszy sposob
# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja', legend=True, title='Populacja na kontynentach', rot=0)

# drugi sposob
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Populacja')
# wykres.set_xlabel('Kontynent')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja na kontynentach')

# mpl.savefig('wykres.png')
# mpl.show()

# ts = pd.Series(np.random.randn((1000)))
# ts = ts.cumsum()
# ts.plot()
# mpl.show()

df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)
grupa = df.groupby('Imie i nazwisko').agg({'Wartosc zamowienia': ['sum']})
grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
mpl.legend(loc='lower right')
mpl.title('Procent zamowienia dla sprzedawcy')
mpl.show()
