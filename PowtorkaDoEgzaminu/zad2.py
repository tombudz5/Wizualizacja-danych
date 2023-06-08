import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('ceny21.xlsx')

fig, axs = plt.subplots()
for i, product in enumerate(df['Rodzaje towarów'].unique()):
    product_data = df[df['Rodzaje towarów'] == product]
    marker = 's' if i % 2 == 0 else '.'
    color = 'pink' if i % 2 == 0 else 'purple'

    axs.scatter(x=product_data['Rok'], y=product_data['Wartość'], color=color, marker=marker, label=product)

plt.xlabel('Rok')
plt.ylabel(f"Cena ({df['Jednostka miary'].unique()[0]})")
plt.title('Wykres cen produktów w danym roku')
plt.text(0.95, 0.05, 'Tomasz Budzejko', transform=axs.transAxes, ha='right', va='bottom')
plt.legend()
plt.savefig('zad2.png')

plt.show()
